"""
Given a string s, return the longest palindromic substring in s.
"""

# n^3
class Solution:
    def longestPalindrome1(self, s: str) -> str:
        max_len = 0
        ans = ""
        
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                candidate = s[i:j]

                if candidate == candidate[::-1] and len(candidate) > max_len:
                    ans = candidate
                    max_len = len(candidate)

        return ans


# n^2
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        ans_len = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > ans_len:
                    ans = s[l:r+1]
                    ans_len = r - l + 1
                l -= 1
                r += 1
                
            # even length
            l, r = i, i +1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > ans_len:
                    ans = s[l:r+1]
                    ans_len = r - l + 1
                l -= 1
                r += 1

        return ans



if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("cbbd"))
