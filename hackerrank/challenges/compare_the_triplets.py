"""
https://www.hackerrank.com/challenges/compare-the-triplets/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def compareTriplets(a, b):
    ans, alice, bob = [], 0, 0

    if a[0] > b[0]:
        alice += 1

    if a[1] > b[1]:
        alice += 1

    if a[2] > b[2]:
        alice += 1

    if a[0] == b[0] or a[1] == b[1] or a[2] == b[2]:
        pass

    if b[0] > a[0]:
        bob += 1

    if b[1] > a[1]:
        bob += 1

    if b[2] > a[2]:
        bob += 1

    ans.append(alice)
    ans.append(bob)

    return ans


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
