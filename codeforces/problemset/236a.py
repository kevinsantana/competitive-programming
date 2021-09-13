def solve():
    user_name = set(input())
    print("CHAT WITH HER!") if len(user_name) % 2 == 0 else print("IGNORE HIM!")


if __name__ == "__main__":
    solve()
