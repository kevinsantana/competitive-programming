def solve():
    n = int(input())
    h = n // 3600
    m = (n % 3600)//60
    s = n % 60
    print(h, ":", m, ":", s, sep="")


if __name__ == "__main__":
    solve()
