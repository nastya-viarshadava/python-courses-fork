import pytest
from tasks.chapter_02_ifelse.my_task05 import find_second_largest

def test_find_second_largest_last():
    assert find_second_largest(3, 5, 4) == 4, "third number is second-largest, should return 4"

def test_find_second_largest_middle():
    assert find_second_largest(7, 9, 1) == 7, "second number is second-largest, should return 7"

def test_find_second_largest_begin():
    assert find_second_largest(16, 0, 2) == 2, "first number is second-largest, should return 2"

def test_find_second_largest_all_equal():
    assert find_second_largest(7, 7, 7) == 7, "all equal, should return 7"

def test_find_second_largest_two_equal_largest():
    assert find_second_largest(7, 9, 9) == 7, "two equal numbers are largest, should return 7"

def test_find_second_largest_middle_two_equal_second_largest():
    assert find_second_largest(7, 8, 7) == 7, "two equal numbers are second-largest, should return 7"

def test_find_second_largest_negative():
    assert find_second_largest(-1, -2, -3) == -2, "first negative number is second-largest, should return -1"

@pytest.mark.parametrize("a, b, c, expected", [
    (100, 99, 98, 99),
    (0, 10, 9, 9),
    (999, 1000, 1, 999),
    (-50, -15, -2, -15),
    (0, 0, 0, 0)
])
def test_second_largest_various_combinations(a, b, c, expected):
    assert find_second_largest(a, b, c) == expected, f"second largest of ({a}, {b}, {c}) should be {expected}"


