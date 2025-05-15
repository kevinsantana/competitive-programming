"""
https://neetcode.io/problems/longest-repeating-substring-with-replacement
"""

from collections import defaultdict


def main(s: str, k: int) -> int:
    l = 0
    longest = 0
    counts = defaultdict(int)

    for r in range(len(s)):
        counts[s[r]] += 1
        win_size = (r - l) + 1

        while win_size - max(counts.values()) > k:
            counts[s[l]] -= 1
            l += 1

        longest = max(longest, win_size)

    return longest

if __name__ == "__main__":
    print(main("XYYX", 2))
    print(main("AAABABB", 1))
