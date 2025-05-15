from typing import List


def solve(gain: List[int]) -> int:
    ans = 0
    altitudes = [0]

    for n in gain:
        ans += n
        altitudes.append(ans)

    return max(altitudes)


if __name__ == "__main__":
    # gain = [-5,1,5,0,-7]
    # expected = 1
    # ans = solve(gain=gain)
    # print(expected, ans)

    gain = [-4,-3,-2,-1,4,3,2]
    expected = 0
    ans = solve(gain=gain)
    print(expected, ans)
