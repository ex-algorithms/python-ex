""" Function that implements Two-fer.

Two-fer or 2-fer is short for two for one. One for you and one for me.

Given a name, return a string with the message:
- 'One for name, one for me.'
Where "name" is the given name.

However, if the name is missing, return the string:
- 'One for you, one for me.'
"""


def two_fer(name="you"):
    """This means 'two for one'.

    :param name: str - name of person sharing, default value is 'you'.
    :return: str - phrase with name of person sharing or default value.

    Function that accepts the name of a person for a two for one sharing
    arrangement, and returns the person's name - or the word 'you', if absent
    - embedded in the standard sharaing pharse.
    """

    return f"One for {name}, one for me."
