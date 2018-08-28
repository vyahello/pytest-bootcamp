from typing import List, Any


def add_one_to_list(lst: List[Any]) -> List[Any]:
    """Add number `1` into the end of given list.
       Return a list.
    """
    lst.append(1)
    return lst


def delete_last_from_list(lst: List[Any]) -> List[Any]:
    """Delete last value from the given list.
       Return a list.
    """
    lst.pop()
    return lst
