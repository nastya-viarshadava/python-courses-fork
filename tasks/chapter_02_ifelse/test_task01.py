import pytest
from task01 import check_number


def test_positive():
    assert check_number(5) == "positive", "positive number should return 'positive'"


def test_negative():
    assert check_number(-3) == "negative", "negative number should return 'negative'"


def test_zero():
    assert check_number(0) == "zero", "zero should return 'zero'"


@pytest.mark.parametrize("num", [1, 42, 999])
def test_many_positive(num):
    assert check_number(num) == "positive", f"{num} should be classified as 'positive'"


@pytest.mark.parametrize("num", [-1, -100, -999])
def test_many_negative(num):
    assert check_number(num) == "negative", f"{num} should be classified as 'negative'"
