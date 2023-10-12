#!/usr/bin/python3
"""a Function that adds 2 integers."""


def add_integer(a, b=98):
    """Return the sum of a and b
        >>> add_integer(1, 2)
        3
        >>> add_integer(100, -2)
        98
    """
    """a Function that adds 2 integers."""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
