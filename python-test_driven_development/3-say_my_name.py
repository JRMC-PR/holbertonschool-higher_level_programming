#!/usr/bin/python3
"""Module for say_my_name method."""


def say_may_name(first_name, last_name=""):
    """_summary_

    Args:
        first_name (_type_): _description_
        last_name (str, optional): _description_. Defaults to "".

    Raises:
        TypeError: _description_
        TypeError: _description_

    >>> say_my_name("John", "Smith")
    My name is John Smith
    >>> say_my_name("Walter", "White")
    My name is Walter White
    >>> say_my_name("Bob")
    My name is Bob
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
