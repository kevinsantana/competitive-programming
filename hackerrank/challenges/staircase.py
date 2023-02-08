"""
https://www.hackerrank.com/challenges/staircase/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#


def staircase(n):
    for i, j in zip(range(n, 0, -1), range(1, n + 1)):
        print(" " * (i - 1), "#" * j, sep="")


if __name__ == "__main__":
    n = int(input().strip())

    staircase(n)
