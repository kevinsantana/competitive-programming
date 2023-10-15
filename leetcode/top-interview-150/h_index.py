"""
https://leetcode.com/problems/h-index
"""

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        h = 0

        if n == 1 and citations[0] == 0:
            return 0
        else:
            for i in range(n):
                if citations[i] < n - i:
                    h = citations[i]
                else:
                    h = max(h, n - i)
            return h


if __name__ == "__main__":
    solve = Solution()
    # citations = [6, 5, 3, 1, 0]
    # print(solve.hIndex(citations))
    # citations = [2, 2, 1]
    # print(solve.hIndex(citations))
    citations = [1, 1, 0]
    print(solve.hIndex(citations))
    citations = [2, 2, 2]
    print(solve.hIndex(citations))
