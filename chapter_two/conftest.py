import pytest


@pytest.fixture(scope="module")
def num():
    return 3
