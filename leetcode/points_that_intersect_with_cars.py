from typing import List


def solve(nums: List[List[int]]) -> int:
    ans = set()
    nums_max = max(nums, key=lambda x: x[1])[1]
    nums_min = min(nums, key=lambda x: x[0])[0]
    line = set(range(nums_min, nums_max + 1))
    for num in nums:
        num_set = set(range(num[0], num[1] + 1))
        ans.update(line.intersection(num_set))

    return len(ans)


if __name__ == "__main__":
    nums = [[3,6],[1,5],[4,7]]
    nums_sorted = [[1,5],[3,6],[4,7]]
    nums_ranged = [[1,2,3,4,5], [3,4,5,6], [4,5,6,7]]
    nums_overlapping = [3,4,5,6,7]
    expected = 7
    ans = solve(nums=nums)
    print(expected, ans)
