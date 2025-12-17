"""
Task 03: Determine the grade based on a score.

Write a function `get_grade(score: int) -> str` that:
- Assume score is between 0 and 100 inclusive
- Returns "A" if score is 90 or above
- Returns "B" if score is 80-89
- Returns "C" if score is 70-79
- Returns "D" if score is 60-69
- The "F" case(if score is below 60), should be implemented later.

Hint
Use Python Pass Statement when score is below 60.
"""

def get_grade(score: int) -> str:
    # TODO: Implement the function
    # Remove 'pass' and write your solution using if/elif/else
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        pass