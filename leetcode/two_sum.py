from typing import List
from itertools import combinations


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for c in combinations(nums, 2):
            if sum(c) == target:
                first_i = nums.index(c[0])
                second_i = nums.index(c[1])

                if c[0] == c[1]:
                    second_i = nums.index(c[1], nums.index(c[0])+1)

                return [first_i, second_i]
        
            

if __name__ == "__main__":
    nums = [3,3]
    target = 6
    s = Solution()
    result = s.twoSum(nums, target)
    print(result)
