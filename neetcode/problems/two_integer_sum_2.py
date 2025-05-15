"""
https://neetcode.io/problems/two-integer-sum-ii
"""


from typing import List


def solve(numbers: List[int], target: int) -> List[int]:
    left = 0
    right = len(numbers) - 1
    while left < right:
        cur_sum = numbers[left] + numbers[right]
        if cur_sum > target:
            right -= 1
        elif cur_sum < target:
            left += 1
        elif cur_sum == target:
            return [left + 1, right + 1]


def main(numbers: List[int], target: int) -> List[int]:
    ans = []
    for i, n in enumerate(numbers):
        for j, m in enumerate(numbers):
            if i == j:
                continue
            if n + m == target:
                ans.append(i+1)
                ans.append(j+1)
                return ans


if __name__ == "__main__":
    cases = [
        ([1,2,3,4], 3, [1,2]),
        ([0,1], 1, [1,2]),
        ([-2, -1, 0, 1, 2], 0, [1, 5])
    ]
    for case in cases:
        numbers = case[0]
        target = case[1]
        expected_ans = case[2]
        ans = solve(numbers=numbers, target=target)
        print(ans)
        assert ans == expected_ans
