import pytest
from tasks.chapter_03_match.task01 import get_day_name


def test_monday():
    assert get_day_name(1) == "Monday", "Day 1 should return 'Monday'"


def test_tuesday():
    assert get_day_name(2) == "Tuesday", "Day 2 should return 'Tuesday'"


def test_wednesday():
    assert get_day_name(3) == "Wednesday", "Day 3 should return 'Wednesday'"


def test_thursday():
    assert get_day_name(4) == "Thursday", "Day 4 should return 'Thursday'"


def test_friday():
    assert get_day_name(5) == "Friday", "Day 5 should return 'Friday'"


def test_saturday():
    assert get_day_name(6) == "Saturday", "Day 6 should return 'Saturday'"


def test_sunday():
    assert get_day_name(7) == "Sunday", "Day 7 should return 'Sunday'"


@pytest.mark.parametrize("day", [0, 8, -1, 10])
def test_invalid_day(day):
    assert get_day_name(day) == "Invalid day", f"Invalid input {day} should return 'Invalid day'"
