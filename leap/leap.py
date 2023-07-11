def leap_year(year):
    verdict = False

    if year % 4 == 0:
        if year % 100 != 0:
            verdict = True
        else:
            if year % 400 == 0:
                verdict = True
            else:
                verdict = False

    return verdict
