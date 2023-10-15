"""
https://leetcode.com/problems/minimum-time-to-complete-trips/
"""

from typing import List
from itertools import zip_longest


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        ans = 0
        total_time = sum(time)
        if len(time) == 1:
            return time[0]
        for time, n_trips in zip_longest(range(1, total_time + 1), time, fillvalue=(x for x in time)):
            if ans == totalTrips:
                break
            if type(n_trips) is int:
                if time % n_trips == 0:
                    ans += 1
            else:
                if time % n_trips.__next__ == 0:
                    ans += 1



if __name__ == "__main__":
    s = Solution()
    time = [1,2,3]
    totalTrips = 5
    print(s.minimumTime(time, totalTrips))
    time = [2]
    totalTrips = 1
    print(s.minimumTime(time, totalTrips))
