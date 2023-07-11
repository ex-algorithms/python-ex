def zero_sides(sides):
    a, b, c = sides

    if a == 0 and b == 0 and c == 0:
        return True


def valid_triangle(info):
    x, y, z = info

    if ((x + y) >= z) and ((x + z) >= y) and ((y + z) >= x):
        return True
    else:
        return False


def equilateral(sides):
    a, b, c = sides

    if a == b and b == c and a == c:
        if zero_sides(sides):
            return False
        else:
            return True
    else:
        return False


def isosceles(sides):
    a, b, c = sides

    if zero_sides(sides):
        return False
    else:
        if a == 1 or b == 1 or c == 1:
            return False
        else:
            if (a == b or a == c) and (b == c or b == a) and (c == a or c == b):
                return True
            else:
                return False


def scalene(sides):
    if valid_triangle(sides):
        if not isosceles(sides) and not equilateral(sides):
            return True

    return False
