"""
https://neetcode.io/problems/duplicate-integer
Contains Duplicate - Leetcode 217 - Python
"""


def solve(nums: list[int]):
    nums_set = set(nums)
    return True if len(nums) > len(nums_set) else False


if __name__ == "__main__":
    nums = [1, 2, 3, 3]
    print(solve(nums))
