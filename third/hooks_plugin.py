from typing import Callable, List
import pytest
from _pytest.fixtures import SubRequest
from _pytest.config import Config
from _pytest.config.argparsing import Parser
from _pytest.python import Function


@pytest.fixture
def hello() -> Callable[..., str]:
    def _hello(request: str = '') -> str:
        if not request:
            return "Hello !"
        return "Hello {}!".format(request)
    return _hello


@pytest.fixture(params=["Brianna", "Andreas", "Floris"])
def name(request: SubRequest) -> str:
    return request.param


def pytest_configure(config: Config) -> None:
    """Enable verbose output when running tests. Simulate ``-v`` option in a command line."""

    config.option.verbose = 1


def pytest_report_header(config: Config) -> List[str]:
    """Add information to test report header."""

    if config.option.verbose > 0:
        return ["Project: pytest-hooks", "Written by: Volodymyr Yahello"]


def pytest_addoption(parser: Parser) -> None:
    """Add custom parameters."""

    parser.addoption("--skip-marker",
                     "-S",
                     action="store",
                     default=None,
                     help="skip test(s) with certain marker.")


def pytest_runtest_setup(item: Function) -> None:
    """Skip tests that belong to specific marker with ``--skip-marker`` cmd option."""

    marker = item.config.getvalue("--skip-marker")
    if marker in item.keywords:
        pytest.skip(f"Skipping [@{marker}] pytest marker")