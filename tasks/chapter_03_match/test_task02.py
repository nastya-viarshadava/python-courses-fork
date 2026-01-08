import pytest
from tasks.chapter_03_match.task02 import classify_age


def test_child():
    assert classify_age(5) == "Child", "Age 5 should be classified as 'Child'"


def test_teenager():
    assert classify_age(15) == "Teenager", "Age 15 should be classified as 'Teenager'"

def test_adult():
    assert classify_age(30) == "Adult", "Age 30 should be classified as 'Adult'"


def test_senior():
    assert classify_age(70) == "Senior", "Age 70 should be classified as 'Senior'"

def test_boundary_child():
    assert classify_age(12) == "Child", "Age 12 should be classified as 'Child'"

def test_boundary_teenager():
    assert classify_age(13) == "Teenager", "Age 13 should be classified as 'Teenager'"
    assert classify_age(19) == "Teenager", "Age 19 should be classified as 'Teenager'"

def test_boundary_adult():
    assert classify_age(20) == "Adult", "Age 20 should be classified as 'Adult'"
    assert classify_age(64) == "Adult", "Age 64 should be classified as 'Adult'"


def test_boundary_senior():
    assert classify_age(65) == "Senior", "Age 65 should be classified as 'Senior'"

@pytest.mark.parametrize("age", [-1, -10])
def test_invalid_age(age):
    assert classify_age(age) == "Invalid age", f"Age {age} should be classified as 'Invalid age'"