"""
https://www.hackerrank.com/challenges/diagonal-difference/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    d_1 = [arr[i][i] for i in range(len(arr))]
    d_2 = [row[-i - 1] for i, row in enumerate(arr)]

    return abs(sum(d_1) - sum(d_2))


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + "\n")

    fptr.close()
