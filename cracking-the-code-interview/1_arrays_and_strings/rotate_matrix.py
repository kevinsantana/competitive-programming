"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
"""

import copy

import numpy as np


def solve(m):
    return [list(reversed(col)) for col in zip(*m)]


def solve_numpy(m):
    new_m = copy.deepcopy(m)
    return np.rot90(new_m, k=1, axes=(1, 0)).tolist()


if __name__ == "__main__":
    m = [
        [1, 2, 3],
        [
            4,
            5,
            6,
        ],
        [7, 8, 9],
    ]
    print(solve(m) == solve_numpy(m))
