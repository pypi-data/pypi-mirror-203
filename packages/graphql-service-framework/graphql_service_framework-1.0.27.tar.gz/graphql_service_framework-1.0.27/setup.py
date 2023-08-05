import io

from setuptools import setup, find_packages

with io.open('README.md', 'rt', encoding='utf8') as f:
    readme = f.read()

with io.open('VERSION') as version_file:
    version = version_file.read().strip().lower()
    if version.startswith("v"):
        version = version[1:]

setup(
    name='graphql_service_framework',
    version=version,
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    author='Robert Parker',
    author_email='rob@parob.com',
    url='https://gitlab.com/parob/graphql-service-framework',
    download_url=f'https://gitlab.com/parob/graphql-service-framework/-/'
                 f'archive/master/graphql-service-framework-v{version}.zip',
    keywords=['GraphQL'],
    description='GraphQL Service Framework.',
    long_description=readme,
    long_description_content_type='text/markdown',
    install_requires=[
        "graphql-core>=3.2.0",
        "graphql-api>=1.2.39",
        "werkzeug>=2.2.2",
        "context-helper>=1.0.2",
        "packaging>=21.3",
        "graphql-schema-diff>=1.2.4",
        "graphql-http-server>=1.3.36",
        "hypercorn>=0.14.3",
        "pytest",
        "pytest-cov",
        "coverage",
        "flake8"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)
