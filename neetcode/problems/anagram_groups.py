"""
https://neetcode.io/problems/anagram-groups
"""

from collections import defaultdict
from typing import List


def main(strs: List[str]) -> List[List[str]]:
    anagrams = defaultdict(list)
    for anagram in strs:
        key = "".join(sorted(anagram))
        anagrams[key].append(anagram)
    print(anagrams)
    return list(anagrams.values())

if __name__ == "__main__":
    print(main(["act","pots","tops","cat","stop","hat"]))
