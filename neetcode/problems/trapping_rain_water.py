"""
https://neetcode.io/problems/trapping-rain-water
"""

from typing import List

def main(height: List[int]) -> int:
    ans = 0
    for i, h in enumerate(height):
        if i == 0:
            return ans
        
        j = i + 1
        left = h[i]
        right = h[j]
        
        if i + 2 < len(height):
            rightmost = h[i+2]
        
        if left > 0 and rightmost > 0 and right != left:
            ans += min(left, rightmost)
            j += 1

def main(height: List[int]) -> int:
    if not height:
        return 0

    n = len(height)
    max_left = [0] * n
    max_right = [0] * n
    trapped_water = 0

    # Calculate max_left array
    max_left[0] = height[0]
    for i in range(1, n):
        max_left[i] = max(max_left[i - 1], height[i])

    # Calculate max_right array
    max_right[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        max_right[i] = max(max_right[i + 1], height[i])

    # Calculate trapped water
    for i in range(n):
        water_level = min(max_left[i], max_right[i])
        if water_level > height[i]:
            trapped_water += water_level - height[i]

    return trapped_water


if __name__ == "__main__":
    print(main([0,2,0,3,1,0,1,3,2,1]))
