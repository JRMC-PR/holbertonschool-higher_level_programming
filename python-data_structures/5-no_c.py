#!/usr/bin/python3
def no_c(my_string):
    new_string = ""  # create a new string
    for i in my_string:  # iterate through the string
        if i != 'c' and i != 'C':
            new_string += i
    return new_string
