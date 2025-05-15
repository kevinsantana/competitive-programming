"""
https://neetcode.io/problems/is-palindrome
"""


def main(s: str) -> bool:
    sanitized_s = ''.join(ch for ch in s.lower().strip() if ch.isalnum())
    return sanitized_s == sanitized_s[::-1]


if __name__ == "__main__":
    cases = [("s", True),
             ("", True),
             (" ", True),
             ("Was it a car or a cat I saw?", True),
             ("tab a cat", False)
    ]
    for case in cases:
        s = case[0]
        expected = case[1]
        ans = main(s=s)
        print(ans)
        assert ans == expected

