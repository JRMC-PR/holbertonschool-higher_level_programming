#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:  # if my_list is not empty
        for i in reversed(my_list):  # go  in reverse order
            print("{:d}".format(i))
