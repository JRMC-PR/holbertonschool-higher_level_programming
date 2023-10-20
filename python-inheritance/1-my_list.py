#!/usr/bin/python3
"""Module that inherits from List"""


class MyList(list):
    """a class that inherits from List"""

    def print_sorted(self):
        """print-sorted
        prints a sorted list
        Arg:
            self: the list

        >>> my_list = MyList()
        >>> my_list.append(1)
        >>> my_list.append(4)
        >>> my_list.append(2)
        >>> my_list.append(3)
        >>> my_list.append(5)
        >>> print(my_list)
        [1, 4, 2, 3, 5]
        >>> my_list.print_sorted()
        [1, 2, 3, 4, 5]
        >>> print(my_list)
        [1, 4, 2, 3, 5]
        >>> my_list = MyList([-1])
        >>> my_list.print_sorted()
        [-1]
        >>> my_list = MyList()
        >>> my_list.print_sorted()
        []
        """
        sortedL = sorted(self)
        print(sortedL)
