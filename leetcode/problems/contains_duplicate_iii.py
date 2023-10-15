"""
https://leetcode.com/problems/contains-duplicate-iii/
"""
from typing import List
from itertools import permutations

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        ans = False
        for c in permutations(nums, r=2):
            candidate1, candidate2 = c[0], c[1]
            
            if candidate1 == candidate2:
                continue

            if abs(candidate1 - candidate2) > indexDiff:
                continue

            candidate1_i, candidate2_i = nums.index(candidate1), nums.index(candidate2)

            if abs(nums[candidate1_i] - nums[candidate2_i]) > valueDiff:
                continue
            
            while nums[candidate1_i] != nums[-1] or nums[candidate2_i] != nums[-1]:

                candidate1_i, candidate2_i = nums.index(candidate1, start=candidate1_i), nums.index(candidate2, start=candidate2_i)
                print(candidate1_i, candidate2_i)

                if abs(nums[candidate1_i] - nums[candidate2_i]) > valueDiff:
                    continue
            
            ans = True

        return ans


if __name__ == "__main__":
    nums = [1,2,3,1]
    indexDiff = 3
    valueDiff = 0
    s = Solution()
    print(s.containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff))
