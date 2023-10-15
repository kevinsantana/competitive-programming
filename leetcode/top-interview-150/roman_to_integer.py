"""
https://leetcode.com/problems/roman-to-integer
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        ans = 0
        for i in range(len(s)):
            if i < len(s) - 1 and roman_to_int[s[i]] < roman_to_int[s[i+1]]:
                ans -= roman_to_int[s[i]]
            else:
                ans += roman_to_int[s[i]]
        
        return ans


if __name__ == "__main__":
    solve = Solution()
    s = "III"
    print(solve.romanToInt(s))
    s = "LVIII"
    print(solve.romanToInt(s))
    s = "MCMXCIV"
    print(solve.romanToInt(s))
