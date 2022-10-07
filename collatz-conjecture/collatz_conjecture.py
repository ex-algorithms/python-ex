def _repeat(num):
    output = 0

    if num % 2 == 0:
        output = num / 2
    else:
        output = (num * 3) + 1

    return output


def steps(number):
    counter = 0

    output = _repeat(number)

    return output


print(_repeat(14))
