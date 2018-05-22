"""
Write a function that finds the longest palindromic substring of a given string. Try to be as efficient as possible!

If you find more than one substring you should return the one which is closer to the beginning.

Input: A text as a string.

Output: The longest palindromic substring.
"""


def longest_palindromic(text):
    for size in reversed(range(len(text))):
        for start in range(len(text) - size):
            sample = text[start:][:size + 1]
            if sample == sample[::-1]:
                return sample


if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
