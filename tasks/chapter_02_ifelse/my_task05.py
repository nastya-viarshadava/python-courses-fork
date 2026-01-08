""""
Task 06: Find the second-largest number
Write a function:
def find_second_largest(a: int, b: int, c: int) -> int:
Rules:
Returns the second largest of the three numbers
Assume numbers can be equal
Do not use sorted() or max()
"""

def find_second_largest(a: int, b: int, c: int) -> int:
    if a >= b >= c:
        return b
    elif b >= a >= c:
        return a
    else:
        return c

