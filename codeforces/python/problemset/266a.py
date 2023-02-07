def solve():
    _, stones = input(), input()
    moves = 0
    for i in range(len(stones) - 1):
        if stones[i] == stones[i + 1]:
            moves += 1
    print(moves)


if __name__ == "__main__":
    solve()
