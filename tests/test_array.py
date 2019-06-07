"""test array alogrithms"""
from src.array import find_peak
from src.array import two_sum_dict
from src.array import two_sum_naive


def test_two_sum_naive():
    """test two sum naive"""
    actual = two_sum_naive([2, 11, 7, 9], target=9)
    expected = (0, 2)
    assert actual == expected

    actual = two_sum_naive([-3, 5, 2, 3, 8, -9], target=0)
    expected = (0, 3)
    assert actual == expected

    actual = two_sum_naive([-3, 5, 2, 3, 8, -9], target=6)
    expected = None
    assert actual == expected


def test_two_sum_dict():
    """test two sum dict"""
    test_cases = (
        ([2, 11, 7, 9], 9, (0, 2)),
        ([-3, 5, 2, 3, 8, -9], 0, (0, 3)),
        ([-3, 5, 2, 3, 8, -9], 6, None),
    )

    for args in test_cases:
        actual = two_sum_dict(*args[:-1])
        expected = args[-1]
        assert actual == expected

        actual = two_sum_naive(*args[:-1])
        expected = args[-1]
        assert actual == expected


def test_find_peak():
    """test find peak recursive"""
    test_cases = (
        ([10, 20, 30, 40, 50], 4),
        ([1, 2, 3, 1], 2),
        ([1], 0),
        ([4, 3, 2, 1], 0),
    )
    for args in test_cases:
        actual = find_peak(*args[:-1])
        expected = args[-1]
        assert actual == expected
