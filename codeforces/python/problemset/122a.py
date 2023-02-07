from math import sqrt


def divisors(n):
    large_divisors = []
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield int(divisor)


def is_lucky(n: int):
    for number in set(str(n)):
        if number not in {"4", "7"}:
            return False
    return True


def solve():
    n = input()
    lucky = False
    for divisor in divisors(int(n)):
        lucky = is_lucky(divisor)
        if lucky:
            break
    print("YES") if lucky or int("".join(n)) % 4 == 0 or int(
        "".join(n)
    ) % 7 == 0 or is_lucky(int(n)) else print("NO")


if __name__ == "__main__":
    solve()
