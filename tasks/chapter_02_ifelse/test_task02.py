import pytest
from task02 import check_even_odd


def test_even():
    assert check_even_odd(4) == "even", "even number should return 'even'"


def test_odd():
    assert check_even_odd(7) == "odd", "odd number should return 'odd'"


def test_zero():
    assert check_even_odd(0) == "even", "zero should be treated as an even number"


@pytest.mark.parametrize("num", [2, 10, 100, 1000])
def test_many_even(num):
    assert check_even_odd(num) == "even", f"The number {num} should return 'even'"


@pytest.mark.parametrize("num", [1, 3, 9, 999])
def test_many_odd(num):
    assert check_even_odd(num) == "odd", f"The number {num} should return 'odd'"
