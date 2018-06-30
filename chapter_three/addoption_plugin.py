import pytest
from _pytest.config.argparsing import Parser
from _pytest.fixtures import SubRequest


def pytest_addoption(parser: Parser) -> None:
    parser.addoption("--host", "-H",
                     action="store",
                     default="localhost",
                     help="A host should be provided as a hostname (google.com) or ip address (172.217.13.238)")


@pytest.fixture(scope="module")
def host(request: SubRequest) -> str:
    return request.config.getoption("--host")
