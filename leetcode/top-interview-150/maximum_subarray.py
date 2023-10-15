"""
https://leetcode.com/problems/maximum-subarray
"""

import math
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ending_here = 0
        max_so_far = -math.inf

        for i in range(len(nums) - 1):
            max_ending_here = max(nums[i], nums[i] + max_ending_here)

            if max_ending_here > max_so_far:
                max_so_far = max_ending_here
            # if max_ending_here < 0:
            #     max_ending_here = 0

            # elif max_so_far < max_ending_here:
            #     max_so_far = max_ending_here           

        # if max_so_far > sum(nums):
        #     return max_so_far
        # else:
        #     return sum(nums)
        return max_so_far


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max = 0
        max_till_now = -math.inf
        for num in nums:
            cur_max = max(num, cur_max + num)
            max_till_now = max(max_till_now, cur_max)
        return max_till_now


if __name__ == "__main__":
    solve = Solution()
    # nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # print(solve.maxSubArray(nums))
    # nums = [1]
    # print(solve.maxSubArray(nums))
    # nums = [5,4,-1,7,8]
    # print(solve.maxSubArray(nums))
    nums = [-2,1,1]
    print(solve.maxSubArray(nums))
