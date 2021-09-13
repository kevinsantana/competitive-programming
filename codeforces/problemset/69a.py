def solve():
    x, y, z = 0, 0, 0
    for _ in range(int(input())):
        tmp = list(map(int, input().split()))
        x += tmp[0]
        y += tmp[1]
        z += tmp[2]
    print("YES") if not any([x, y, z]) else print("NO")
    
    
if __name__ == "__main__":
    solve()
