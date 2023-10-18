#!/usr/in/python3
"""Module that inherits from List"""


class MyList(list):
    """a class that inherits from List"""

    def print_sorted(self):
        """print-sorted
        prints a sorted list
        Arg:
            self: the list

        """
        print(sorted(self))
