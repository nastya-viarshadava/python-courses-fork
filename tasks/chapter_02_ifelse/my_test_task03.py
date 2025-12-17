import pytest
from task03 import get_grade

def test_a():
    assert get_grade(95) == "A", "score >= 90 should get 'A'"

def test_b():
    assert get_grade(80) == "B", "score >= 80 should get 'B'"

def test_c():
    assert get_grade(79) == "C", "score >= 70 should get 'C'"

def test_d():
    assert get_grade(61) == "D", "score >= 60 should get 'D'"

def test_f():
    assert get_grade(59) == None, "'F' should be implemented later"