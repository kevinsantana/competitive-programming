"""
https://www.hackerrank.com/challenges/mini-max-sum/
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    if len(set(arr)) > 1:
        arr.sort()
        min_sum = sum(arr[: arr.index(max(arr))])
        max_sum = sum(arr[arr.index(min(arr)) + 1 :])
        print(min_sum, max_sum)
    else:
        print(sum(arr[1:]), sum(arr[1:]))


if __name__ == "__main__":
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
