"""
https://neetcode.io/problems/is-anagram
Valid Anagram - Leetcode 242
"""

def solve(s: str, t: str):
    if len(s) != len(t):
        return False
    sorted_s = sorted(s)
    sorted_t = sorted(t)
    for l, r in zip(sorted_s, sorted_t):
        if l != r:
            return False
    return True

def solve_cleaver(s, t):
    return sorted(s) == sorted(t)


if __name__ == "__main__":
    s = "racecar"
    t = "carrace"
    # s = "jar"
    # t = "jam"
    print(solve(s, t))
