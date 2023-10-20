#!/usr/bin/python3
"""0. Read file"""


def read_file(filename=""):
    """
    function that reads a text file (UTF8) and prints it to stdout
    Args:
        filename: name of the file
    """
    with open('my_file_0.txt', 'r', encoding='utf-8') as f:
        print(f.read(), end="")
