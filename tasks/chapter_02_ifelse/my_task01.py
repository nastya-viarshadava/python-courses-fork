""""
Write a function:
def check_parity(num: int) -> str:
That:
Returns "even" if the number is divisible by 2
Returns "odd" if the number is not divisible by 2
Returns "zero" if the number is 0
"""

# a = 9%2
# print(a)

def check_parity(num: int) -> str:
    if num == 0:
        return "zero"
    elif num % 2 == 0:
        return "even"
    else:
        return "odd"

