"""
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z)
"""

from itertools import groupby


def solve(s: str):
    compressed = ""
    for g in ["".join(g) for k, g in groupby(s)]:
        compressed += f"{''.join(set(g))}{len(g)}"

    if len(compressed) < len(s):
        return compressed
    else:
        return s


if __name__ == "__main__":
    s = "aaabbbcccccaadddeeeefffffghijk"
    print(solve(s))
