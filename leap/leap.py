"""Determine whether year is a leap year according to the Gregorian calendar."""


def leap_year(year):
    """
    :param year: int - year of choice.
    :return: bool - is this a leap year?
    """

    verdict = False

    if year % 4 == 0:
        verdict = True

    if year % 100 == 0:
        verdict = False

    if year % 4 == 0 and year % 100 != 0:
        verdict = True

    if year % 100 == 0 and year % 400 == 0:
        verdict = True

    return verdict
