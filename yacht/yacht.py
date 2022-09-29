""" Determine number of scores in a Yacht dice game - https://en.wikipedia.org/wiki/Yacht_(dice_game). """

# Score categories.
# Change the values as you see fit.
YACHT = None
ONES = None
TWOS = None
THREES = None
FOURS = None
FIVES = None
SIXES = None
FULL_HOUSE = None
FOUR_OF_A_KIND = None
LITTLE_STRAIGHT = None
BIG_STRAIGHT = None
CHOICE = None


def score(dice, category):
    """Calculate the number of scores in the game, based on the selected category.

    :param dice: list - a list of numbers holding dice faces.
    :param category: bool - boolean contained in a constant variable.
    :return: int - score based on category selected, zero if category no applicable.
    """

    dice.sort()

    return dice


# scaffolding
print(score([2, 4, 1, 5, 2], ""))
