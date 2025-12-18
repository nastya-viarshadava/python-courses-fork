import pytest
from my_tdd_task import is_even

def test_is_even():
    assert is_even(4) is True, "even numbers should be True"

def test_is_uneven():
    assert is_even(5) is False, "uneven numbers should be False"

def test_zero_is_even():
    assert is_even(0) is True, "zero should be True"

def test_negative_is_even():
    assert is_even(11) is False

@pytest.mark.parametrize("num, expected",[
    (1, False),
    (9, False),
    (10, True),
    (100, True),
    (99, False)
])
def test_is_even(num, expected):
    assert is_even(num) is expected, f"{num} return {expected}"