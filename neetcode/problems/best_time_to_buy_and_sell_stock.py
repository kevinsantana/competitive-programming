"""
https://neetcode.io/problems/buy-and-sell-crypto
"""

from typing import List


def main(prices: List[int]) -> int:
    ans = 0
    for i, price in enumerate(prices):
        if i + 1 < len(prices):
            profit = max(prices[i+1:]) - price
            ans = max(ans, profit)

    return ans


if __name__ == "__main__":
    print(main([10,1,5,6,7,1]))
    print(main([10,8,7,5,2]))
