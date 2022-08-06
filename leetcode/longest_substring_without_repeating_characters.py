from itertools import combinations


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        if len(s) == 2:
            if len(set(s)) == 1:
                return len(set(s))
            return len(s)

        ans = []
        for i in range(len(s)):
            for l in combinations(s[i:], i + 1):
                if len(set(l)) < len(s):
                    ans.append(l)
                else:
                    ans.append(set(l))

        return len(max(ans, key=len))


# not my solution
# https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1731/A-Python-solution-85ms-O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        curr_max = 0
        for index, letter in enumerate(s):
            if letter in seen and left <= seen[letter]:
                left = seen[letter] + 1
            else:
                curr_max = max(curr_max, index - left + 1)
            seen[letter] = index

        return curr_max


if __name__ == "__main__":
    word = "cdd"
    s = Solution()
    result = s.lengthOfLongestSubstring(word)
    print(result)
