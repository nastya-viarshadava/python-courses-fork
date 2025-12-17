import pytest
from my_task01 import check_parity


def test_even():
    assert check_parity(4) == "even", "number should return 'even'"


def test_odd():
    assert check_parity(3) == "odd", "number should return 'odd'"


def test_zero():
    assert check_parity(0) == "zero", "zero should return 'zero'"


@pytest.mark.parametrize("num", [2, 42, 1000])
def test_many_even(num):
    assert check_parity(num) == "even", f"{num} should be classified as 'even'"


@pytest.mark.parametrize("num", [1, -99, 999])
def test_many_odd(num):
    assert check_parity(num) == "odd", f"{num} should be classified as 'odd'"
