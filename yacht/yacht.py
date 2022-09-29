""" Determine number of scores in a Yacht dice game - https://en.wikipedia.org/wiki/Yacht_(dice_game). """

# Default constants
YACHT = None
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = None
FOUR_OF_A_KIND = None
LITTLE_STRAIGHT = None
BIG_STRAIGHT = None
CHOICE = "choice"

# Internal constants
_SINGLES = [ONES, TWOS, THREES, FOURS, FIVES, SIXES]


def _singles(dice, number):
    """Calculates the score for single dice game options.

    :param dice: list - a list of numbers holding dice faces.
    :param number: int - a number describing a single dice game option.
    :return: int - a count of the selected number multiplied by the number.
    """

    mapping = {ONES: 1, TWOS: 2, THREES: 3, FOURS: 4, FIVES: 5, SIXES: 6}

    counter = 0

    for el in dice:
        if el == mapping[number]:
            counter += 1

    return counter * number


def score(dice, category):
    """Calculate the number of scores in the game, based on the selected category.

    :param dice: list - a list of numbers holding dice faces.
    :param category: bool - boolean contained in a constant variable.
    :return: int - score based on category selected, zero if category no applicable.
    """

    dice.sort()

    score = 0

    if category in _SINGLES:
        score = _singles(dice, category)

    if category == "choice":
        score = sum(dice)

    # return score, "|", dice
    return score


# # scaffolding
print(score([5, 5, 1, 5, 2], CHOICE))
# print(_singles([5, 5, 1, 5, 2], FIVES))
