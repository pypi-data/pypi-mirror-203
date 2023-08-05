import asyncio
import inspect
import os

from typing import Dict

from graphql_api import GraphQLAPI
from graphql_api.remote import GraphQLRemoteObject, GraphQLRemoteExecutor
from graphql_api.utils import to_snake_case
from graphql_http_server import GraphQLHTTPServer

from hypercorn import Config
from hypercorn.asyncio import serve
from hypercorn.typing import ASGIFramework, WSGIFramework
from hypercorn.middleware import AsyncioWSGIMiddleware


class Service:

    def __init__(self, root, config: Dict = None):
        from graphql_service_framework import ServiceConnection, \
            ServiceManager

        if not config:
            config = {}

        self.config = config

        graphiql_default = self.config.get("graphiql_default", "")
        relative_path = self.config.get("http_relative_path", "")

        if not self.config.get("service_type"):
            self.config["service_type"] = "asgi"

        if not self.config.get("service_name"):
            self.config["service_name"] = to_snake_case(
                root.__class__.__name__
            )

        if not self.config.get("api_version"):
            self.config["api_version"] = root.__class__.api_version

        if not self.config.get("http_health_path"):
            self.config["http_health_path"] = f"{relative_path}/health"

        health_path = self.config.get("http_health_path")

        if not graphiql_default:
            # noinspection PyBroadException
            try:
                dirname = os.path.dirname(inspect.getfile(root.__class__))
                graphiql_default = open(
                    os.path.join(dirname, '../graphiql_default.graphql'),
                    mode='r'
                ).read()
            except Exception:
                # noinspection PyBroadException
                try:
                    dirname = os.path.dirname(inspect.getfile(root.__class__))
                    graphiql_default = open(
                        os.path.join(dirname, '../.graphql'),
                        mode='r'
                    ).read()
                except Exception:
                    pass

        self.graphql_api = GraphQLAPI(root=root.__class__)
        self.graphql_http_server = GraphQLHTTPServer.from_api(
            api=self.graphql_api,
            root_value=root,
            graphiql_default_query=graphiql_default,
            health_path=health_path
        )

        self.service_manager_path = self.config.get(
            'service_manager_path', "/service"
        )

        connections = []

        for key, service in self.config.get('services', {}).items():
            from graphql_service_framework.schema import Schema
            valid_service = False

            if inspect.isclass(service) and issubclass(service, Schema):
                service = service.client()

            if isinstance(service, GraphQLRemoteObject):
                if issubclass(service.python_type, Schema):
                    version = service.python_type.api_version.split('.')

                    if isinstance(service.executor, GraphQLRemoteExecutor):
                        version = f"~={version[0]}.{version[1]}"
                        url = service.executor.url + self.service_manager_path
                        connection = ServiceConnection(
                            name=key,
                            schema=service.python_type,
                            api_version_specifier=version,
                            service_url=service.executor.url,
                            service_manager_url=url
                        )

                        connections.append(connection)
                        valid_service = True

            if not valid_service:
                raise TypeError(f"Invalid service {key} {service}.")

        self.service_manager = ServiceManager(
            name=config.get("service_name"),
            api_version=config.get("api_version"),
            connections=connections
        )

    def create_wsgi_app(self) -> WSGIFramework:
        from graphql_service_framework import ServiceMeshMiddleware

        wsgi_app = self.graphql_http_server.app(main=self.config.get("main"))
        return ServiceMeshMiddleware(
            wsgi_app=wsgi_app,
            service_manager=self.service_manager,
            service_manager_path=self.service_manager_path
        )

    def create_app(self) -> ASGIFramework:
        return AsyncioWSGIMiddleware(
            wsgi_app=self.create_wsgi_app(),
            max_body_size=2 ** 32
        )

    def run(self, config: Dict = None):
        asyncio_config = Config.from_mapping({
            **(self.config or {}),
            **(config or {})
        })

        return asyncio.run(serve(
            self.create_app(), asyncio_config
        ))

    def client(self):
        from werkzeug.test import Client

        return Client(self.create_wsgi_app())
