""" Determine number of scores in a Yacht dice game - https://en.wikipedia.org/wiki/Yacht_(dice_game). """

# Default constants
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
CHOICE = "choice"
LITTLE_STRAIGHT = [1, 2, 3, 4, 5]
BIG_STRAIGHT = [2, 3, 4, 5, 6]
FULL_HOUSE = "full_house"
FOUR_OF_A_KIND = "four_of_a_kind"
YACHT = "yacht"

# Internal constants
_SINGLES = [ONES, TWOS, THREES, FOURS, FIVES, SIXES]
_SIMILARITIES = [FULL_HOUSE, FOUR_OF_A_KIND, YACHT]


# Internal functions
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


def _straights(dice, category, options):
    """Assigns straight game option score after dice analysis.

    :param dice: list - a list of numbers holding dice faces.
    :param category: bool - boolean contained in a constant variable.
    :return: int - Thirty (30) if dice contains correct straight game numbers.
    """

    output = 0

    for el in options:
        if category == el == dice:
            output = 30

    return output


def _similarities(dice, category):
    """Calculates game output based on dice number similarities.

    :param dice: list - a list of numbers holding dice faces.
    :param category: bool - boolean contained in a constant variable.
    :return: int - output score based on relevant category standard.
    """

    output = 0

    reps = dict()

    for x in dice:
        reps[f"{dice.count(x)}s"] = x

    for key, value in reps.items():
        if key == "5s" and category == "yacht":
            output = 50

        if key == "5s" and category == "four_of_a_kind":
            output = reps["5s"] * 4

        if key == "3s" and category == "full_house":
            output = sum(dice)

        if key == "4s" and category == "four_of_a_kind":
            output = reps["4s"] * 4

    return output


# Exercise function
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

    if category == LITTLE_STRAIGHT or category == BIG_STRAIGHT:
        score = _straights(dice, category, [LITTLE_STRAIGHT, BIG_STRAIGHT])

    if category in _SIMILARITIES:
        score = _similarities(dice, category)

    return score
