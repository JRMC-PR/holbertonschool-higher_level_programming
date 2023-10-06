#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return None
    # next line is a list comprehension
    for key, data in sorted(a_dictionary.items()):
        print(f"{key}: {data}")
