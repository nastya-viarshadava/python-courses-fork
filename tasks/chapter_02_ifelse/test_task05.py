import pytest
from task05 import find_largest

def test_largest_first():
    assert find_largest(5, 3, 1) == 5, "first number is the largest, should return 5"


def test_largest_second():
    assert find_largest(2, 7, 4) == 7, "second number is the largest, should return 7"


def test_largest_third():
    assert find_largest(1, 2, 9) == 9, "third number is the largest, should return 9"


def test_all_equal():
    assert find_largest(3, 3, 3) == 3, "all numbers are equal, should return 3"


def test_negative_numbers():
    assert find_largest(-1, -5, -3) == -1, "first negative number is the largest, should return -1"


@pytest.mark.parametrize("a, b, c, expected", [
    (10, 5, 8, 10),
    (1, 10, 5, 10),
    (5, 8, 10, 10),
    (0, 0, 0, 0),
    (-10, -5, -15, -5),
])
def test_various_combinations(a, b, c, expected):
    assert find_largest(a, b, c) == expected, f"largest of ({a}, {b}, {c}) should be {expected}"
