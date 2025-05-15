"""
https://neetcode.io/problems/longest-consecutive-sequence
"""

from typing import List


def solve(nums: List[int]) -> int:
    num_set = set(nums)
    longest = 0
    for num in nums:
        if (num - 1) not in num_set:
            length = 0
            while (num + length) in num_set:
                length += 1
            longest = max(length, longest)
    
    return longest



def main(nums: List[int]) -> int:
    ans = []
    nums.sort()
    for i, num in enumerate(nums):
        if i == 0:
            ans.append(num)
            continue
        if abs(ans[-1] - num) == 1:
            ans.append(num)
        ans = []
        ans.append(num)
        import ipdb; ipdb.set_trace()

    print(ans)
    return len(ans)



if __name__ == "__main__":
    # numbers = [0,0]
    # ans = main(nums=numbers)
    # print(ans)
    # assert ans == 1

    # numbers = [-2,-1]
    # ans = main(nums=numbers)
    # print(ans)
    # assert ans == 2

    # numbers = []
    # ans = main(nums=numbers)
    # print(ans)
    # assert ans == 0

    # numbers = [1]
    # ans = main(nums=numbers)
    # print(ans)
    # assert ans == 1

    numbers = [9,1,4,7,3,-1,0,5,8,-1,6]
    ans = main(nums=numbers)
    print(ans)
    assert ans == 7
