"""
Input: One positional argument as an iterable or two or more positional arguments. Optional keyword argument as a function.

Output: The largest item for the "max" function and the smallest for the "min" function.
"""


def min(*args, **kwargs):
    key = kwargs.get('key', None)
    rev = kwargs.get('rev', False)
    return sorted(args if len(args) > 1 else args[0], key=key, reverse=rev)[0]


def max(*args, **kwargs):
    key = kwargs.get('key', None)
    return min(*args, key=key, rev=True)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
