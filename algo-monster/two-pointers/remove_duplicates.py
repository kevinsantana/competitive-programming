"""
https://algo.monster/problems/remove_duplicates
"""

def solve(arr: list) -> int:
    if len(arr) <= 2:
        return len(arr)

    left, right = 0, 1

    for i in range(len(arr)):
        if left < len(arr) and right < len(arr):
            if arr[left] == arr[right]:
                arr.remove(arr[right])
                right += 1
            
            else:
                left = right + 1
                right = left + 1

    print(arr)
    return len(arr)


def remove_duplicates(nums) -> int:
    slow, fast = 0, 1
    while fast in range(len(nums)):  # dont get out of boundaries
        if nums[slow] == nums[fast]:
            fast += 1
        else:
            nums[slow + 1] = nums[fast]
            fast += 1
            slow += 1

    return slow + 1


if __name__ == "__main__":
    arr = [0, 0, 1, 1, 1, 2, 2]
    print(remove_duplicates(arr))
