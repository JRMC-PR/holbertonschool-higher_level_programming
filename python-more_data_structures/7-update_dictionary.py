#!/usr/bin/python3
"""
    Update the dictionary `a_dictionary` with the key-value pair `(key, value)`.
    If `key` is already in the dictionary, update its value to `value`.
    If `key` is not in the dictionary, add the key-value pair `(key, value)` to the dictionary.
    Return the updated dictionary.
    """


def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        a_dictionary[key] = value
        return a_dictionary
    else:
        a_dictionary.setdefault(key, value)
        return a_dictionary
