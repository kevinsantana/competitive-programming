def solve():
    a, b, c, d = map(int, input().split())
    print(
        "Valores aceitos"
    ) if b > c and d > a and c + d > a + b and a % 2 == 0 else print(
        "Valores nao aceitos"
    )


if __name__ == "__main__":
    solve()
