"""
https://leetcode.com/problems/merge-sorted-array
"""

from copy import copy
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tmp = sorted(nums1[:m] + nums2)
        nums1.clear()
        nums1.extend(tmp)


if __name__ == "__main__":
    s = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    s.merge(nums1, m, nums2, n) == [1, 2, 2, 3, 5, 6]
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    s.merge(nums1, m, nums2, n)
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    s.merge(nums1, m, nums2, n)
    nums1 = [-5, -4, -3, -2, -1, 0, 0, 0, 0, 0]
    m = 5
    nums2 = [-5, -4, -3, -2, -1]
    n = 3
    s.merge(nums1, m, nums2, n)
    nums1 = [0,0,0,0,0]
    m = 0
    nums2 = [1,2,3,4,5]
    n = 5
    s.merge(nums1, m, nums2, n)