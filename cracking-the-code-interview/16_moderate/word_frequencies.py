"""
Word Frequencies: Design a method to find the frequency of occurrences of any given word in a
book. What if we were running this algorithm multiple times?
"""

import re
from collections import defaultdict


def solve(s: str):
    freq = defaultdict(int)
    regex_str = "[^A-Za-z0-9 ]+"
    new_s = re.sub(regex_str, "", s).lower()
    for word in new_s.split():
        freq[word] += 1
    
    return freq


if __name__ == "__main__":
    s = "Space: The Final Frontier"
    print(solve(s))
