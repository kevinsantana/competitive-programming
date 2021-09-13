import functools


@functools.lru_cache()
def banana_cost(k, w):
    if w == 1:
        return k
    return k + banana_cost(k, w-1)


def solve():
    k, n, w = map(int, input().split())
    total = 0
    for i in range(1, w+1):
        total += banana_cost(k, i)
    print(total - n) if total > n else print(0)
    

if __name__ == "__main__":
    solve()
