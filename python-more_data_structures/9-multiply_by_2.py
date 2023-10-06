#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        b_dictionary = a_dictionary.copy()
        b_dictionary = {key: value * 2 for key, value in a_dictionary.items()}
    return b_dictionary
