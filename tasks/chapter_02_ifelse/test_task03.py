import pytest
from task03 import get_grade


def test_grade_a():
    assert get_grade(95) == "A", "score 95 should return grade 'A'"
    assert get_grade(90) == "A", "score 90 should return grade 'A'"


def test_grade_b():
    assert get_grade(85) == "B", "score 85 should return grade 'B'"
    assert get_grade(80) == "B", "score 80 should return grade 'B'"


def test_grade_c():
    assert get_grade(75) == "C", "score 75 should return grade 'C'"
    assert get_grade(70) == "C", "score 70 should return grade 'C'"


def test_grade_d():
    assert get_grade(65) == "D", "score 65 should return grade 'D'"
    assert get_grade(60) == "D", "score 60 should return grade 'D'"


def test_grade_f_not_implemented():
    # Because of `pass`, Python returns None
    assert get_grade(59) is None, "score below 60 should return None (not implemented)"
    assert get_grade(0) is None, "score 0 should return None (not implemented)"


@pytest.mark.parametrize("score, expected", [
    (100, "A"),
    (89, "B"),
    (79, "C"),
    (69, "D"),
    (59, None),
])
def test_various_grades(score, expected):
    assert get_grade(score) == expected, f"score {score} should return {expected}"
