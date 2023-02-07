"""
Smallest Difference: Given two arrays of integers, compute the pair of values (one value in each
array) with the smallest (non-negative) difference. Return the difference.
EXAMPLE
Input: {1, 3, 15, 11, 2}, {23, 127,235, 19, 8}
Output: 3. That is, the pair (11, 8).
"""

from math import inf


def solve_brute_force(a, b):
    min = inf
    if len(a) == 0 or len(b) == 0:
        return -1
    for i in range(len(a)):
        for j in range(len(b)):
            if abs(a[i] - b[j]) < min:
                min = abs(a[i] - b[j])

    return min


def solve(a, b):
    a.sort()
    b.sort()
    diff, i, j = inf, 0, 0

    while i < len(a) and j < len(b):
        if abs(a[i] - b[j]) < diff:
            diff = abs(a[i] - b[j])

        if a[i] < b[j]:
            i += 1
        else:
            j += 1

    return diff


if __name__ == "__main__":
    a = [1, 3, 15, 11, 2]
    b = [23, 127, 235, 19, 8]
    print(solve_brute_force(a, b))
    print(solve(a, b))
