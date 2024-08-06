"""
Question: List all duplicates in an array or a list. Return type is also an array or a list
"""


from collections import defaultdict


def solve(nums):
    duplicates = defaultdict(int)
    for n in nums:
        duplicates[n] += 1

    return [n for n in duplicates.values() if n > 1]


if __name__ == "__main__":
    nums = [1,2,2,3,4]
    print(solve(nums))
