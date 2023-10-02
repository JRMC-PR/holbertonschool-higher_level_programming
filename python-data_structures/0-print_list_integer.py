#!/usr/bin/python3
def priny_list_integer(my_list=[]):  # function that prints all integers
    for i in range(len(my_list)):  # loop through list
        print("{:d}".format(my_list[i]))  # print each element
