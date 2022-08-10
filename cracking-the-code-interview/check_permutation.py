"""
Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.
"""

from collections import Counter
from itertools import permutations


def solve_bruteforce(one: str, other: str):
    """
    O(n!)
    """
    perms = permutations(one, r=len(one))
    if other in perms:
        return True
    else:
        return False


def solve(one: str, other: str):
    if len(one) != len(other):
        return False
    sorted_one = sorted(one)
    sorted_other = sorted(other)
    return len(sorted_one) == len(sorted_other)


def solve_clever(one: str, other: str):
    if len(one) != len(other):
        return False
    one_count, other_count = Counter(one), Counter(other)
    if one_count != other_count:
        return False
    else:
        return True


if __name__ == "__main__":
    a = "abvfdghhhha"
    b = "avbfdghhhha"
    print(solve_clever(a, b))
