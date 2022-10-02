"""Identifies whether or not input digits make up an Armstrong number. """


def is_armstrong_number(number):
    """Determines whether or not an input is an Armstrong number.

    :param number: int - input number to be tested.
    :return: bool - True, if input is an armstrong number.
    """

    # change int to string
    block = str(number)

    # create dictionary data structure
    number_context = dict()

    # add number of digits to dictionary
    number_context["digits"] = len(block)

    # create list for digit items
    number_pieces = list()

    # loop over number string to attach digits to list
    for el in block:
        number_pieces.append(int(el))

    number_context["content"] = number_pieces

    # test sum of number context items using Armstrong number logic
    sum_test = 0

    for key, value in number_context.items():
        if key == "content":
            for el in number_context[key]:
                sum_test += el ** number_context["digits"]

    # test whether test sum and input number are equal
    armstrong = False

    if sum_test == number:
        armstrong = True

    # return boolean for Armstrong test results
    return armstrong
