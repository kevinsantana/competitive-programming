"""
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.
"""


def solve(m):
    for i in range(len(m)):
        if 0 in m[i]:
            m[i] = [0 * x for x in m[i]]
        else:
            for c in m[i]:
                if c == 0:
                    m[i][0 : len(m[i])] = [x[0] * 0 for x in m]
    return m


if __name__ == "__main__":
    m = [[1, 0, 3], [4, 5, 6], [7, 8, 0]]
    print(solve(m))
