"""
https://www.hackerrank.com/challenges/magic-square-forming
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#


def formingMagicSquare(s):
    used = set()
    for x in s:
        for y in x:
            used.add(y)
    not_used = set(range(1, 10)) - used

    for i in range(len(s)):
        for j in range(len(s[i])):
            pass


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + "\n")

    fptr.close()
