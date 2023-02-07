def solve():
    n = int(input())
    anos = n // 365
    meses = (n % 365) // 30
    dias = (n % 365) % 30
    print(f"{anos} ano(s)", f"{meses} mes(es)", f"{dias} dia(s)", sep="\n")


if __name__ == "__main__":
    solve()
