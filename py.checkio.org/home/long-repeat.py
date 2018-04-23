"""
This mission is the first one of the series. Here you should find the length of the longest substring that consists
 of the same letter. For example, line "aaabbcaaaa" contains four substrings with the same letters "aaa", "bb","c"
 and "aaaa". The last substring is the longest one which makes it an answer.

Input: String.

Output: Int.
"""

import re


def long_repeat(line):
    lst = [item[0] for item in re.findall(r"((.)\2*)", line)]  # ['s', 'd', 's', 'ffff', 's', 'e']

    lengs = [len(l) for l in lst]  # [1, 1, 1, 4, 1, 1]

    try:
        return max(lengs)
    except:
        return 0


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')