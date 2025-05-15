"""
https://algo.monster/problems/move_zeros
"""

def solve(nums):
    write_idx = 0
    for read_idx in range(len(nums)):
        if nums[read_idx] != 0:
            nums[write_idx], nums[read_idx] = nums[read_idx], nums[write_idx]
            write_idx += 1
    return nums


if __name__ == "__main__":
    arr = [1, 0, 2, 0, 0, 7]
    print(solve(arr))
