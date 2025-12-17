"""
Task 01: Check if a number is positive, negative, or zero.

Write a function `check_number(num: int) -> str` that:
- Returns "positive" if the number is greater than 0
- Returns "negative" if the number is less than 0
- Returns "zero" if the number is 0
"""


def check_number(num: int) -> str:
    # TODO: Implement the function
    # Remove 'pass' and write your solution using if/else
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"


