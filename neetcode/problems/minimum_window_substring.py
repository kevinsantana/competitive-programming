"""
https://neetcode.io/problems/minimum-window-with-characters
"""

from collections import Counter

def main(s: str, t: str) -> str:
    len_s = len(s)
    len_t = len(t)
    ans = ""
    min_len = float('inf')

    if len_s < len_t:
        return ""
    
    count_t = Counter(t)
    
    for i in range(len_s + 1):
        substring_window = s[:i]

        if len(substring_window) < len_t:
            continue

        substring_count = Counter(substring_window)
        
        is_valid_window = True
        for char, required_count in count_t.items():
            if substring_count[char] < required_count:
                is_valid_window = False
                break
        
        if is_valid_window:
            current_len = len(substring_window)
            if current_len < min_len:
                min_len = current_len
                ans = substring_window

    return ans


def main(s: str, t: str) -> str:
    if len(s) < len(t) or not t:
        return ""
    
    window = {}
    count_t = {}

    for c in t:
        count_t[c] = 1 + count_t.get(c, 0)

    need, have = len(count_t), 0
    ans, ans_len = [-1,-1], float("inf")
    l = 0

    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c, 0)

        if c in count_t and window[c] == count_t[c]:
            have += 1

        while have == need:
            if (r - l + 1) < ans_len:
                ans = [l, r]
                ans_len = (r - l + 1)
            window[s[l]] -= 1
            if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                have -= 1
            l += 1

    l, r = ans

    return s[l:r+1] if ans_len != float("inf") else ""
    
    
    



if __name__ == "__main__":
    print(main(s="OUZODYXAZV", t="XYZ"))
