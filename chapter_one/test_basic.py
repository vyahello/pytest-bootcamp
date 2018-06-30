from chapter_one.operation import increment


def test_increment() -> None:
    assert increment(2) == 3
