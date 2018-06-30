import pytest
import sys
from chapter_one.operation import length


@pytest.mark.skip(reason="I just want to skip this test.")
def test_skip_length() -> None:
    assert length('12') == 2


@pytest.mark.skipif(sys.platform == 'win32', reason='Does not support 32bit Windows platform')
def test_skipif_length() -> None:
    assert length('12') == 2


@pytest.mark.xfail(reason="Expected failure.")
def test_exp_fail_length() -> None:
    assert length(None) == 1


@pytest.mark.parametrize("test_input, expected_output", [
    ('', 0),
    ('1', 1),
    ('123', 3)
])
def test_param_length(test_input: str, expected_output: int) -> None:
    assert length(test_input) == expected_output


@pytest.mark.own_marker
def test_own_marker_length() -> None:
    assert length([1, 2]) == 2
