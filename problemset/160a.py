def solve():
    n = int(input())
    coins = sorted(map(int, input().split()))
    my_coins, min_coins = 0, 0
    for _ in range(n):
        if my_coins > sum(coins):
            return min_coins
        my_coins += coins.pop()
        min_coins += 1
    return min_coins


if __name__ == "__main__":
    print(solve())
