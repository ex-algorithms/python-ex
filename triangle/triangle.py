"""Identify the type of triangle based on an argument list of sides."""


def _zero_length_sides(sides):
    """Searches triangle sides input for zero.

    :param sides: a list of sides in the triangle to be tested.
    :return: True, if any side is zero in length.
    """
    verdict = False

    for el in sides:
        if el == 0:
            verdict = True

    return verdict


def equilateral(sides):
    """Identifies whether a triangle is equilateral.

    :param sides: a list of sides in the triangle to be tested.
    :return: True, if all sides are of equal length.
    """
    verdict = False

    if max(sides) == min(sides):
        verdict = True

    if _zero_length_sides(sides):
        verdict = False

    return verdict


def isosceles(sides):
    pass


def scalene(sides):
    pass
