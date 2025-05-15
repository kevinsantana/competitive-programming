"""
https://leetcode.com/problems/merge-k-sorted-lists/description/
"""

from itertools import chain
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_i=None):
        self.val = val
        self.next = next_i

    def __iter__(self):
        pass

def solve(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    return sorted(chain.from_iterable(lists))


if __name__ == "__main__":
    lists = [[1,4,5],[1,3,4],[2,6]]
    expected = [1,1,2,3,4,4,5,6]
    print(solve(lists))

    lists = []
    expected = []
    print(solve(lists))

    lists = [[]]
    expected = []
    print(solve(lists))
