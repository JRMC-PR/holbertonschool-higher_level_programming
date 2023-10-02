#!/usr/bin/python3
def print_list_integer(my_list=[]):  # defines prints list function
    for i in range(len(my_list)):  # for loop to iterate through list
        print("{:d}".format(my_list[i]))  # prints list with format specifier
