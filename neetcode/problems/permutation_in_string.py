"""
https://neetcode.io/problems/permutation-string
"""

from collections import defaultdict

# def main(s1: str, s2: str) -> bool:
#     l = 0
#     if not s2:
#         return False
#     import ipdb; ipdb.set_trace()
#     for r in range(len(s2)):
#         substring = ""
#         if s2[r] in s1:
#             while r < len(s2) and s2[r] in s1:
#                 substring += s2[r]
#                 r += 1

#         if sorted(substring) == sorted(s1):
#             return True
        
#         l += 1
        
#     return False


# def main(s1: str, s2: str) -> bool:
#     n1 = len(s1)
#     n2 = len(s2)
    
#     if n1 > n2:
#         return False

#     s1_counts = defaultdict(int)
#     s2_counts = defaultdict(int)

#     for i in range(n1):
#         s1_counts[s1[i]] += 1
#         s2_counts[s2[i]] += 1

#     if s1_counts.values() == s2_counts.values():
#         return True
    

#     for i in range(n1, n2):
#         s2_counts[s2[i]] += 1
#         s2_counts[s2[i - n1]] -= 1

#         if s1_counts.values() == s2_counts.values():
#             return True

#     return False


def main(s1: str, s2: str) -> bool:
    n1 = len(s1)
    n2 = len(s2)
    
    if n1 > n2:
        return False

    for i in range(n2):
        substring_window = s2[i:n1+i]
        print(substring_window)

        if sorted(s1) == sorted(substring_window):
            return True
        
    return False

def solve(s1: str, s2: str) -> bool:
    n1 = len(s1)
    n2 = len(s2)
    counts_s1 = defaultdict(int)
    
    if n1 > n2:
        return False
    
    for c in s1:
        counts_s1[c] += 1

    for i in range(n2):
        substring_window = s2[i:n1+i]
        counts_w = defaultdict(int)

        for c in substring_window:
            counts_w[c] += 1

        if counts_s1 == counts_w:
            return True
    
    return False


if __name__ == "__main__":
    # print(main("abc", "lecabee"))
    # print(main("abc", "lecaabee"))
    # print(main("a", "a"))
    # print(main("", ""))
    # print(main("aaaa", "aaaa"))
    # print(main("ab", "eidboaoo"))
    assert True == main("ab", "cccccbabbbaaaa")
