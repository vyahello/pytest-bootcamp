from second.square import square_list


def test_square_list(num: int) -> None:
    assert square_list(num) == [1, 4]


def test_len_square_list(num: int) -> None:
    assert len(square_list(num)) == 2
