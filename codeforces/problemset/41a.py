def my_reverse(word: str) -> str:
    drow = ""
    for i in range(len(word), 0, -1):
        drow += word[i-1]
    return drow


def solve():
    s, t = input(), input()
    print("YES") if s == my_reverse(t) else print("NO")


if __name__ == "__main__":
    solve()
