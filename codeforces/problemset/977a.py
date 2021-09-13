def solve():
    n, k = map(int, input().split())
    for _ in range(k):
        if n % 10 != 0:
            n -= 1
        elif n % 10 == 0:
            n = n//10
    print(n)
        
            
if __name__ == "__main__":
    solve()
