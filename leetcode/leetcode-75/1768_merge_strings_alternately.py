from itertools import zip_longest


def solve(word1: str, word2: str):
    ans = ""
    for w1, w2 in zip_longest(word1, word2, fillvalue=""):
        ans += w1 + w2
    return ans

if __name__ == "__main__":
    word1 = "ab"
    word2 = "pqrs"
    print(solve(word1, word2))