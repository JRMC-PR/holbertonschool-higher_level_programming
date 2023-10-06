#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        if my_list is None:
            return 0
        for i in range(0, x):
            print(f"{my_list[i]}", end="")
        print()
        return i + 1
    except (IndexError, TypeError, ValueError):
        print()
        return i
