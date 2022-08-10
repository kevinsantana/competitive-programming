"""
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters,and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: "Mr John Smith ", 13
Output: "Mr%20John%20Smith"
"""


def solve_bruteforce(s: str):
    urlify_space = "%20"
    return s.replace(" ", urlify_space)


def solve_no_ds(s: str):
    urlify_space = "%20"
    new_s = ""
    for i in range(len(s)):
        if ord(s[i]) == 32:
            new_s += urlify_space
        else:
            new_s += s[i]
    return new_s


if __name__ == "__main__":
    s = "Mr John Smith "
    print(solve_no_ds(s))
