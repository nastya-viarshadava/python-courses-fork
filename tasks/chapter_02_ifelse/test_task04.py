import pytest
from task04 import is_leap_year


def test_leap_year_2000():
    assert is_leap_year(2000) is True, "year 2000 should be a leap year (divisible by 400)"


def test_leap_year_2020():
    assert is_leap_year(2020) is True, "year 2020 should be a leap year (divisible by 4)"


def test_not_leap_year_1900():
    assert is_leap_year(1900) is False, "year 1900 should NOT be a leap year (divisible by 100 but not 400)"


def test_not_leap_year_2021():
    assert is_leap_year(2021) is False, "year 2021 should NOT be a leap year"


def test_leap_year_2024():
    assert is_leap_year(2024) is True, "year 2024 should be a leap year (divisible by 4)"


@pytest.mark.parametrize("year, expected", [
    (1600, True),
    (1700, False),
    (1800, False),
    (1900, False),
    (2000, True),
    (2020, True),
    (2021, False),
    (2024, True),
    (2100, False),
])
def test_various_years(year, expected):
    assert is_leap_year(year) is expected, f"year {year} should return {expected}"
