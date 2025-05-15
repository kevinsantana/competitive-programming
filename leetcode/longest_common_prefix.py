"""
https://leetcode.com/problems/longest-common-prefix/description/
"""

from collections import defaultdict
from typing import List


def solve(strs: List[str]) -> str:
    ans = defaultdict(int)
    for word in strs:
        for char in word:
            ans[char] += 1
    return


if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    expected = "fl"
    ans = solve(strs=strs)
    print(expected, ans)
