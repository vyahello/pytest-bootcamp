import pytest


@pytest.fixture(scope="function")
def function_setup() -> str:
    print("executes for every test function")
    return "function_setup"


@pytest.fixture(scope="module")
def module_setup() -> str:
    print("executes once for module before all tests")
    return "module_setup"


@pytest.fixture(scope="class")
def class_setup() -> str:
    print("executes before every class")
    return "class_setup"


@pytest.fixture(scope="session")
def session_setup() -> str:
    print("executes once for a session")
    return "session_setup"


def test_module_one(module_setup: str) -> None:
    print('running test_module_one')
    assert module_setup == "module_setup"


def test_module_two(module_setup: str) -> None:
    print('running test_module_two')
    assert module_setup == "module_setup"


def test_function_one(function_setup: str) -> None:
    print('running test_function_one')
    assert function_setup == "function_setup"


def test_function_two(function_setup: str) -> None:
    print('running test_function_two')
    assert function_setup == "function_setup"


def test_session_one(session_setup: str) -> None:
    print('running test_session_one')
    assert session_setup == "session_setup"


def test_session_two(session_setup: str) -> None:
    print('running test_session_two')
    assert session_setup == "session_setup"


class TestOne:
    def test_class_one(self, class_setup: str) -> None:
        print('running test_class_one')
        assert class_setup == "class_setup"


class TestTwo:
    def test_class_two(self, class_setup: str) -> None:
        print('running test_class_two')
        assert class_setup == "class_setup"