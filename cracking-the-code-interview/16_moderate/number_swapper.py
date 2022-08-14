"""
Number Swapper: Write a function to swap a number in place (that is, without temporary vari
ables).
"""


def solve(a, b):
    """
    a > b
    """
    a = a - b
    b = a + b
    a = b - a
    return a


def solve_binary(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a


if __name__ == "__main__":
    a, b = 16, 11
    print(solve(a, b))
    print(solve_binary(a, b))
