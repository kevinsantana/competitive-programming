from typing import List
from itertools import combinations


def my_eq(one, other):
    if len(one) != len(other):
        return False
    new_one = sorted(one)
    new_other = sorted(other)
    for i, j in zip(new_one, new_other):
        if i != j:
            return False
    return True


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(set(nums)) == 0:
            return [nums]
        result = []
        for c in combinations(nums, 3):
            if sum(c) == 0:
                result.append(c)

        ans = []
        for i in range(len(result) + 1):
            for j in result[i:]:
                if not my_eq(list(result[i]), list(j)):
                    ans.append(list(j))

        return ans


# not my solution
# https://leetcode.com/problems/3sum/discuss/7498/python-solution-with-detailed-explanation
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        N, result = len(nums), []
        for i in range(N):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = nums[i] * -1
            s, e = i + 1, N - 1
            while s < e:
                if nums[s] + nums[e] == target:
                    result.append([nums[i], nums[s], nums[e]])
                    s = s + 1
                    while s < e and nums[s] == nums[s - 1]:
                        s = s + 1
                elif nums[s] + nums[e] < target:
                    s = s + 1
                else:
                    e = e - 1
        return result


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    s = Solution()
    ans = s.threeSum(nums)
    print(ans)
