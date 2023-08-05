import pytest

from context_helper import ctx
from graphql_api import field
from werkzeug import Response
from werkzeug.test import Client

from graphql_http_server import GraphQLHTTPServer
from graphql_service_framework.middleware import ServiceMeshMiddleware
from graphql_service_framework.mesh import \
    ServiceConnection, \
    ServiceManager
from tests.utils import available


class TestServiceManager:

    utc_time_url = \
        "https://europe-west2-parob-297412.cloudfunctions.net/utc_time"

    # noinspection DuplicatedCode,PyUnusedLocal
    @pytest.mark.skipif(
        not available(utc_time_url),
        reason=f"The UTCTime API '{utc_time_url}' is unavailable"
    )
    def test_service_manager(self):
        from graphql_api import GraphQLAPI

        class UTCTimeSchema:

            @field
            def now(self) -> str:
                pass

        connections = [ServiceConnection(
            name="utc_time",
            service_url=self.utc_time_url,
            schema=UTCTimeSchema
        )]

        service_manager = ServiceManager(
            name="gateway",
            api_version="0.0.1",
            connections=connections
        )

        api = GraphQLAPI()

        @api.type(root=True)
        class RootQueryType:

            @api.field
            def hello(self, name: str) -> str:
                utc_time: UTCTimeSchema = ctx.services["utc_time"]

                return f"hey {name}, the time is {utc_time.now()}"

        server = GraphQLHTTPServer.from_api(api=api)

        client = Client(
            ServiceMeshMiddleware(
                server.app(),
                service_manager,
                "/service"
            ),
            Response
        )

        response = client.get('/service?query={logs}')

        assert response.status_code == 200
        assert "ServiceState = OK" in response.text

        response = client.get('/?query={hello(name:"rob")}')

        assert response.status_code == 200
        assert "rob" in response.text
        assert "20" in response.text
