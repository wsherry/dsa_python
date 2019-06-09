"""test array alogrithms"""
from src.pattern_match import boyer_moore


def test_booyer_moore():
    """test booyer_moore"""
    test_cases = (
        ("ABBCBBD", "BC", [2]),
        ("ABBCBEBCBD", "BC", [2, 6]),
        ("BCBCBC", "BC", [0, 2, 4]),
    )

    for * args, expected in test_cases:
        assert list(boyer_moore(*args)) == expected
