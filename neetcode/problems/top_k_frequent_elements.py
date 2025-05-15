"""
https://neetcode.io/problems/top-k-elements-in-list
"""

from collections import Counter, defaultdict
from typing import List


def main(nums: List[int], k: int) -> List[int]:
    ans = Counter(nums)
    return sorted(x[0] for x in ans.most_common(n=k))


def main_2(nums: List[int], k: int) -> List[int]:
    ans = defaultdict(int)
    for elem in nums:
        ans[elem] +=1
    return [x[0] for x in sorted(ans.items(), key=lambda item: item[1], reverse=True)][:k]


if __name__ == "__main__":
    ans = main(nums=[1,2,2,3,3,3], k=2)
    print(ans)
    assert ans == [2, 3]
    ans2 = main_2(nums=[1,1,1,2,2,3], k=2)
    print(ans2)
    assert ans2 == [1,2]
