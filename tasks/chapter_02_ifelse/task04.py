"""
Task 04: Check if a year is a leap year.

Write a function `is_leap_year(year: int) -> bool` that:
- Returns True if the year is a leap year
- Returns False otherwise
- A year is a leap year if it is divisible by 4, but not by 100 unless it is also divisible by 400

Hint
Use Python Logical Operators for simultaneous check division by 4, 100 and 400.
"""

def is_leap_year(year: int) -> bool:
    # TODO: Implement the function
    # Remove 'pass' and write your solution using if/else
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False