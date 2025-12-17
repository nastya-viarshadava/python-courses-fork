"""
Task 02: Check if a number is even or odd.

Write a function `check_even_odd(num: int) -> str` that:
- Returns "even" if the number is even
- Returns "odd" if the number is odd
"""

def check_even_odd(num: int) -> str:
    # TODO: Implement the function
    # Remove 'pass' and write your solution using if/else
    if num == 0:
        return "even"
    elif num % 2 == 0:
        return "even"
    else:
        return "odd"