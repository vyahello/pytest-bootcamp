import sys
import pytest


@pytest.mark.system
def test_platform() -> None:
    assert sys.platform == 'darwin'


@pytest.mark.system
def test_python_version() -> None:
    assert sys.version_info[:3] == (3, 7, 0)