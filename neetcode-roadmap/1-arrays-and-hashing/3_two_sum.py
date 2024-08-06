"""
https://neetcode.io/problems/two-integer-sum

Two Sum - Leetcode 1
"""

def solve(nums: list[int], target: int):
    """
    Brute force O(n^2)
    """
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            if nums[i] + nums[j] == target:
                return [i, j]


def solve_cleaver(nums, target):
    hashmap = {}
    ans = []
    for idx, n in enumerate(nums):
        if (target - n) in hashmap:
            ans.append(nums.index(target - n))
            ans.append(idx)
        else:
            hashmap[n] = idx

    return ans


if __name__ == "__main__":
    nums = [3,4,5,6]
    target = 7
    print(solve_cleaver(nums, target))
