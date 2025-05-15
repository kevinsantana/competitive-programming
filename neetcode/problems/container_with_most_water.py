"""
https://neetcode.io/problems/max-water-container
"""

from typing import List


def brute_force(heights: List[int]) -> int:
    ans = 0

    for l in range(len(heights)):
        for r in range(l + 1, len(heights)):
            area = (r - l) * min(heights[l], heights[r])
            ans = max(ans, area)

    return ans


def main(heights: List[int]) -> int:
    ans = 0
    l, r = 0, len(heights) - 1

    while l < r:
        area = (r - l) * min(heights[l], heights[r])
        ans = max(ans, area)

        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1

    return ans


if __name__ == "__main__":
    main()
