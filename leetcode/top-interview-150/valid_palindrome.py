import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = re.sub(r'[\W_]+', "", s.lower())
        return True if clean_s == clean_s[::-1] else False


if __name__ == "__main__":
    solve = Solution()
    s = "A man, a plan, a canal: Panama"
    print(solve.isPalindrome(s))
    s = "race a car"
    print(solve.isPalindrome(s))
    s = " "
    print(solve.isPalindrome(s))
