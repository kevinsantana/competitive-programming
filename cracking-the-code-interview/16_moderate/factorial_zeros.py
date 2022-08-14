"""
Factorial Zeros: Write an algorithm which computes the number of trailing zeros in n factorial.
"""


def solve(n):
    count = 0
    for i in range(1, n):
        if i % 5 == 0:
            count += 1

    return count


if __name__ == "__main__":
    n = 700  # expected 174
    print(solve(n))
