"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""
from typing import List
from statistics import median


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        k = sorted([*nums1, *nums2])
        return median(k)


if __name__ == "__main__":
    s = Solution()
    n = [1, 2]
    m = [3, 4]
    print(s.findMedianSortedArrays(n, m))
