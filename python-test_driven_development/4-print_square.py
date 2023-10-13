#!/usr/binptyhon3
def print_square(size):
    """
    Prints a square with the character #.
    >>> print_square(4)
    ####
    ####
    ####
    ####
    >>> print_square(10)
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    >>> print_square(0)

    >>> print_square(1)
    #
    >>> print_square(-1)
    Traceback (most recent call last):
        ...
    ValueError: size must be >= 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
