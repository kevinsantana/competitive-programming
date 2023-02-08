"""
https://www.hackerrank.com/challenges/plus-minus/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    lenght = len(arr)
    p, n, z = 0, 0, 0

    p = lambda x: [y for y in x if y > 0]
    n = lambda x: [y for y in x if y < 0]
    z = lambda x: [y for y in x if y == 0]

    print(
        f"{len(p(arr))/lenght:.6f}",
        f"{len(n(arr))/lenght:.6f}",
        f"{len(z(arr))/lenght:.6f}",
        sep="\n",
    )


if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
