"""Identify the type of triangle based on an argument list of sides."""


def _triangle_equal(sides):
    """Determines whether or not a triangle's sides are equal.

    :param sides: list - a list of sides in the triangle to be tested.
    :return: bool - True, if triangle sides are equal.
    """
    a, b, c = sides

    verdict = False

    if a + b >= c and a + c >= b and b + c >= a:
        verdict = True

    return verdict


def _zero_length_sides(sides):
    """Searches triangle sides input for zero.

    :param sides: list - a list of sides in the triangle to be tested.
    :return: bool - True, if any side is zero in length.
    """
    verdict = False

    for el in sides:
        if el == 0:
            verdict = True

    return verdict


def equilateral(sides):
    """Identifies whether a triangle is equilateral.

    :param sides: list - a list of sides in the triangle to be tested.
    :return: bool - True, if all sides are of equal length.
    """
    verdict = False

    if max(sides) == min(sides):
        verdict = True

    if _zero_length_sides(sides):
        verdict = False

    return verdict


def isosceles(sides):
    """Determines if a triangle is an isosceles.

    :param sides: list - a list of sides in the triangle to be tested.
    :return: bool - True, if two sides are of equal length.
    """

    a, b, c = sides

    verdict = False

    if a == b or a == c:
        verdict = True
    elif b == a or b == c:
        verdict = True
    elif c == a or c == b:
        verdict = True

    if not _triangle_equal(sides):
        verdict = False

    return verdict


def scalene(sides):
    pass


print(isosceles([3, 5, 3]))
