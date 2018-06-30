from typing import Iterable
from chapter_three.operation import total, count


def test_total(rng: Iterable[int]) -> None:
    assert total(rng) == 10


def test_count(rng: Iterable[int]) -> None:
    assert count(rng) == 5
