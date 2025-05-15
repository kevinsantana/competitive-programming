from collections import defaultdict


def solve(pattern: str, s: str) -> bool:
    ans = defaultdict(str)
    pattern_set = set(pattern)
    words_set = set(s.split(" "))

    if len(pattern_set) != len(words_set):
        return False

    for word in words_set:
        s = pattern_set.pop()
        if s not in ans:
            ans[s] = word
    return ans

if __name__ == "__main__":
    # pattern = "abba"
    # s = "dog cat cat dog"
    # expected = True
    # ans = solve(pattern=pattern, s=s)
    # print(expected, ans)

    # pattern = "abcb"
    # s = "dog cat dog cat"
    # expected = False
    # ans = solve(pattern=pattern, s=s)
    # print(expected, ans)

    # pattern = "abcb"
    # s = "dog cat hat cat"
    # expected = True
    # ans = solve(pattern=pattern, s=s)
    # print(expected, ans)

    pattern = "aba"
    s = "cat cat cat dog"
    expected = False
    ans = solve(pattern=pattern, s=s)
    print(expected, ans)
