import pytest
from typing import Iterable


@pytest.fixture(scope='module')
def rng() -> Iterable[int]:
    return range(5)
