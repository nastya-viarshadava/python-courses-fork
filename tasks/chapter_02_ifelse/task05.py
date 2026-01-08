"""
Task 05: Find the largest of three numbers.

Write a function `find_largest(a: int, b: int, c: int) -> int` that:
- Returns the largest of the three integers a, b, and c

Hint
Use Python Comparison Operators to compare the numbers.
"""

def find_largest(a: int, b: int, c: int) -> int:
    # TODO: Implement the function
    # Remove 'pass' and write your solution using if/elif/else
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    else:
        return False