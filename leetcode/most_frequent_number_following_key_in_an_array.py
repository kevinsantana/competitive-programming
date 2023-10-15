"""
https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/
"""

from typing import List
from collections import Counter


class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        arr = [nums[i + 1] for i in range(len(nums) - 1) if nums[i] == key]
        c = Counter(arr)
        return max(c, key=c.get)


if __name__ == "__main__":
    nums = [1,100,200,1,100]
    key = 1
    s = Solution()
    print(s.mostFrequent(nums, key))
    nums = [2,2,2,2,3]
    key = 2
    s = Solution()
    print(s.mostFrequent(nums, key))
