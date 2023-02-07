def solve():
    x = int(input())
    result = 0
    while x != 0:
        result += x // 5
        x = x - (x // 5 * 5)

        result += x // 4
        x = x - (x // 4 * 4)

        result += x // 3
        x = x - (x // 3 * 3)

        result += x // 2
        x = x - (x // 2 * 2)

        result += x // 1
        x = x - (x // 1 * 1)
    print(result)


if __name__ == "__main__":
    solve()
