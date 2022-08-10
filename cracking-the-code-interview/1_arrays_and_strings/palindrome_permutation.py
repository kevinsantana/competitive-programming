"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin
drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.)
"""
import re
from collections import Counter, defaultdict


def frequency(s: str):
    freq = defaultdict(int)
    for i in range(len(s)):
        freq[s[i]] += 1

    return freq


def solve(s: str):
    regex_str = "[^A-Za-z0-9 ]+"
    new_s = re.sub(regex_str, "", s).lower()
    s_count = Counter(new_s)
    odd_char = False

    for i in s_count.values():
        if i % 2 == 1:
            if odd_char:
                return False
            odd_char = True

    return odd_char


if __name__ == "__main__":
    s = "tactcoapapa"
    print(solve(s))
    # print(frequency(s))
