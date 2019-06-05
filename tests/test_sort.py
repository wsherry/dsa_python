"""test sorting alogrithms"""
from src.sort import (
    insertion_sort,
    insertion_sort_optimized,
    selection_sort,
    merge_sort,
)


def test_insertion_sort():
    """test insertion sort"""
    actual = insertion_sort([1, 5, 65, 23, 57, 1232])
    expected = [1, 5, 23, 57, 65, 1232]
    assert actual == expected


def test_insertion_sort_optimized():
    """test insertion sort optimized"""
    actual = insertion_sort_optimized([1, 5, 65, 23, 57, 1232])
    expected = [1, 5, 23, 57, 65, 1232]
    assert actual == expected


def test_selection_sort():
    """test selection sort"""
    actual = selection_sort([1, 5, 65, 23, 57, 1232])
    expected = [1, 5, 23, 57, 65, 1232]
    assert actual == expected


def test_merge_sort():
    """test merge sort"""
    actual = merge_sort([1, 5, 65, 23, 57, 1232])
    expected = [1, 5, 23, 57, 65, 1232]
    assert actual == expected
