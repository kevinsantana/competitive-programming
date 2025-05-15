"""
https://leetcode.com/problems/k-closest-points-to-origin/
"""

import heapq
from math import sqrt
from typing import List


def solve(points: List[List[int]], k: int) -> List[List[int]]:
    origin = [0, 0]
    ans = []
    
    def euclidian_distance(point: List[List[int]]):
        return sqrt((point[0] - origin[0])**2 + (point[1] - origin[1])**2)
    
    for point in points:
        heapq.heappush(ans, (euclidian_distance(point), point))

    return [heapq.heappop(ans)[1] for _ in range(k)]



if __name__ == "__main__":
    # points = [[1,3],[-2,2]]
    # k = 1
    # print(solve(points=points, k=k))

    # {(3, 3): 4.242640687119285, (5, -1): 5.0990195135927845, (-2, 4): 4.47213595499958}
    points = [[3,3],[5,-1],[-2,4]]
    k = 2
    expected = [[3,3], [-2,4]]
    print(solve(points=points, k=k))
