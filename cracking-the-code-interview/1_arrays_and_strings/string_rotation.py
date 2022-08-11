"""
String Rotation:Assume you have a method isSubstring which checks if one word is a substring
of another. Given two strings, sl and s2, write code to check if s2 is a rotation of s1 using only one
call to isSubstring (e.g.,"waterbottle" is a rotation of "erbottlewat").
"""


def is_substring(s1: str, s2: str) -> bool:
    return True if s2 in s1 else False


def solve(s1: str, s2: str) -> bool:
    return True if is_substring("".join(sorted(s1)), "".join(sorted(s2))) else False


if __name__ == "__main__":
    s1 = "waterbottle"
    s2 = "erbottlewat"
    print(solve(s1, s2))
