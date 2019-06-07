"""test array alogrithms"""
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
    actual = two_sum_dict([2, 11, 7, 9], target=9)
    expected = (0, 2)
    assert actual == expected

    actual = two_sum_dict([-3, 5, 2, 3, 8, -9], target=0)
    expected = (0, 3)
    assert actual == expected

    actual = two_sum_dict([-3, 5, 2, 3, 8, -9], target=6)
    expected = None
    assert actual == expected
