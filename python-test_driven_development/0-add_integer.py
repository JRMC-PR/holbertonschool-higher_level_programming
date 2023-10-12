#!/usr/bin/python3
"""add_integer - function
Attribute:
    a: first integer
    b: second integer
return: sum of a and b"""


def add_integer(a, b=98):
    """Returns sum of a and b
        >>> add_integer(100, -2)
        98  """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
