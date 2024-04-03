"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40


def bake_time_remaining(bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - bake_time


def preparation_time_in_minutes(num_of_layers):
    """Calculate preparation time in minutes

    :param num_of_layers: int - number of baking layers used.
    :return: int - required preparation time left.

    Function that takes the required number of layers per recipe.
    """
    return num_of_layers * 2


def elapsed_time_in_minutes(num_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking minutes.

    :param num_of_layers: int - number of baking layers used.
    :param elapsed_bake_time: int - number of minutes passed since baking commenced.
    :return: int - total estimated cooking time in minutes.

    Function that takes the number of layers and elapsed bake time and returns the estimated cooking time in minutes.
    """
    return preparation_time_in_minutes(num_of_layers) + elapsed_bake_time

