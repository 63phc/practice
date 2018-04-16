"""
A game's result is presented as a list of strings, where "X" and "O" are players' marks and "." is the empty cell.

Input: A game result as a list of strings (unicode).

Output: "X", "O" or "D" as a string.
"""


def checkio(game_result):
    sample = ''.join(game_result)
    all_result = (game_result +
                         [sample[i::3] for i in range(3)] +
                         [sample[0::4]] +
                         [sample[2:7:2]])
    if 'XXX' in all_result:
        return 'X'
    elif 'OOO' in all_result:
        return 'O'
    else:
        return 'D'


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

