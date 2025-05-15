"""
https://neetcode.io/problems/anagram-groups

Leetcde - 49. Group Anagrams
"""

def is_anagram(first: str, second: str) -> bool:
    if "".join(sorted(first)) == "".join(sorted(second)):
        return True
    return False


def solve(strs: list):
    if len(strs) == 1:
        return strs

    ans = []
    l = 0
    r = len(strs) - 1

    for i in range(len(strs)):
        l = i
        if l == r:
            return ans
        
        if is_anagram(strs[l], strs[r]):
            ans.append([strs[r], strs[l]])

        r -= 1



if __name__ == "__main__":
    strs = [""]
    print(solve(strs))
