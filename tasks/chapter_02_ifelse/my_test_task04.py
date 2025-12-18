import pytest
from my_task04 import is_valid_username

# positive_username
# positive_username_isalnum
# positive_first_character
#
# negative_username
# negative_username_isalnum
# negative_first_character
#
# positive_boundaries_partitioning
# negative_boundaries_partitioning

def test_positive_username():
    assert is_valid_username("natalie") is True, "username should be at least 5 characters"

def test_positive_username_isalnum():
    assert is_valid_username("natalie1") is True, "username should contain only letters and digits"

def test_positive_first_character():
    assert is_valid_username("natalie") is True, "username shouldn't start with a digit"

def test_negative_username():
    assert is_valid_username("nat") is False, "username should be at least 5 characters"

def test_negative_username_isalnum():
    assert is_valid_username("natalie#") is False, "username should contain only letters and digits"

def test_negative_first_character():
    assert is_valid_username("5natalie") is False, "username shouldn't start with a digit"

@pytest.mark.parametrize("username, expected", [
    ("maria", True),
    ("mari", False),
    ("mariam", True),
    ("", False),
    (" ", False),
    ("a", False),
    ("0maria", False),
    ("555maria", False)
])
def test_boundaries_analysis(username, expected):
    assert is_valid_username(username) is expected, f"{username} should return {expected}"

