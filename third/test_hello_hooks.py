from typing import Callable


def test_hello_default(hello: Callable[..., str]) -> None:
    assert hello() == "Hello !"


def test_hello_name(hello: Callable[..., str], name: str) -> None:
    assert hello(name) == "Hello {0}!".format(name)
