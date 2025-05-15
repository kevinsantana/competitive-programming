"""
https://neetcode.io/problems/products-of-array-discluding-self

division op?
"""

from functools import lru_cache, reduce
from operator import mul
from typing import List


def main(nums: List[int]) -> List[int]:
    ans = []
    for i, n in enumerate(nums):
        except_self = nums.copy()
        except_self.pop(i)

        @lru_cache
        def _apply_mul(except_self: List[int]):
            return reduce(mul, except_self)

        ans.append(_apply_mul(except_self=tuple(except_self)))

    return ans


if __name__ == "__main__":
    ans = main(nums=[-1,0,1,2,3])
    print(ans)
    assert ans == [0,-6,0,0,0]

    ans = main(nums=[0,0])
    print(ans)
    assert ans == [0,0]

    ans = main(nums=[1,2,4,6])
    print(ans)
    assert ans == [48,24,12,8]
