from typing import Any, Iterable


def increment(number: int) -> int:
    """Increment a given number by `1`."""
    return number + 1


def to_int(element: Any) -> int:
    """Convert given element into `int` data type."""
    return int(element)


def length(itr: Iterable[Any]) -> int:
    """Count elements in iterable object."""
    return len(itr)


def square(number: int):
    """Calculate square of a given number."""
    return number ** 2
