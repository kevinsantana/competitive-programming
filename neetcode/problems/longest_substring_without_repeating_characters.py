"""
https://neetcode.io/problems/longest-substring-without-duplicates
"""

# def main(word: str) -> int:
#     ans = 0
#     left, right = 0, 1
#     for i in range(len(word)):
#         while word[left] != word[right]:
#             right += 1
#             longest = right - left
#             ans = max(ans, longest)
#         left = right
#         right = left
    
#     return ans

def main(s: str) -> int:
    if not s:
        return 0

    n = len(s)
    max_length = 0
    left = 0

    for right in range(n):
        current_char = s[right]
        substring_window = s[left:right]

        if current_char in substring_window:
            duplicate_index = s.index(current_char, left)
            left = duplicate_index + 1

        current_length = right - left + 1
        max_length = max(max_length, current_length)
    
    return max_length


def solve(s: str) -> int:
    if not s:
        return 0

    n = len(s)
    longest = 0
    left = 0
    char_set = set()

    for right in range(n):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        w = (right - left) + 1
        longest = max(longest, w)
        char_set.add(s[right])
    
    return longest



if __name__ == "__main__":
    print(main("zxyzxyz"))
    print(main("xxxx"))
    print(main("xxyy"))
