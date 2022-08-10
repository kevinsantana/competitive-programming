"""
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
"""

from itertools import zip_longest


def solve(s: str, t: str):
    # equal size, check if is one edit away or more
    if len(s) == len(t):
        count_diff = 0
        for c, h in zip(s, t):
            if c != h:
                count_diff += 1
        if count_diff > 1:
            return False
        else:
            return True
    else:
        for i, j in zip_longest(s, t, fillvalue="'"):
            try:
                if s.index(i) != t.index(j):
                    if i != j:
                        return False
            except ValueError:
                continue
    return True


if __name__ == "__main__":
    s, t = "pale", "bake"
    print(solve(s, t))
