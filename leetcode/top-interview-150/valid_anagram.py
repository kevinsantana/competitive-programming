from itertools import zip_longest


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sort, t_sort = sorted(s), sorted(t)
        for letter_s, letter_t in zip_longest(s_sort, t_sort):
            if letter_s != letter_t:
                return False
        return True
        


if __name__ == "__main__":
    solve = Solution()
    s = "anagram"
    t = "nagaram"
    print(solve.isAnagram(s, t))
    s = "rat"
    t = "car"
    print(solve.isAnagram(s, t))
    s = "aacc"
    t = "ccac"
    print(solve.isAnagram(s, t))
    s = "ac"
    t = "c"
    print(solve.isAnagram(s, t))
