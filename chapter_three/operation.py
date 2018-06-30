from typing import Iterable


def total(rng: Iterable[int]) -> int:
    return sum(rng)


def count(rng: Iterable[int]) -> int:
    return len(rng)
