import re


def solve():
    s = input()
    print("YES") if re.findall(r'\w*h\w*e\w*l\w*l\w*o\w*', s) else print("NO")


if __name__ == "__main__":
    solve()
