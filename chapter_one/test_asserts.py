import pytest
from chapter_one.operation import to_int


def test_to_int() -> None:
    assert to_int('5') == 5


def test_to_int_two_asserts() -> None:
    assert to_int('5') == 5
    assert to_int(10.0) == 10


def test_to_int_expected_exception() -> None:
    with pytest.raises(TypeError, message="Expecting TypeError"):
        to_int(None)