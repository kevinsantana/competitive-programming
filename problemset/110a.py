def is_lucky(n: str):
    for number in n:
        if number not in {"4", "7"}:
            return False
    return True


def is_digits_lucky(n: str):
    digits_lucky = 0
    for number in n:
        if number in {"4", "7"}:
            digits_lucky += 1
    return is_lucky(str(digits_lucky))


def solve():
    n = input()
    print("YES") if is_digits_lucky(n) else print("NO")

    
if __name__ == "__main__":
    solve()
