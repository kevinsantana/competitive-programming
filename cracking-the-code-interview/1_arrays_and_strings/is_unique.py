"""
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
"""


def solve(s: str):
    dict_char = {y: x for x, y in enumerate(s)}
    if len(dict_char) == len(s):
        return True
    else:
        return False


def solve_no_ds(s: str):
    for i in range(len(s) - 1):
        for j in range(len(s[i:])):
            if s[i] == s[j]:
                return False
    return True


if __name__ == "__main__":
    s = "fuiogweouifgwehfkowghnjkowernjgiopwerngiowbguioweuiweghfujiwehfjiowe"
    ans = solve(s)
    ans1 = solve_no_ds(s)
    assert ans == ans1
