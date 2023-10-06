#!/usr/bin/python3
"""
Delete the key-value pair with the specified `key` from the dictionary
`a_dictionary`.
If `key` is not in the dictionary, do nothing.
If `key` is an empty string, do nothing.
Return the updated dictionary.
"""


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        a_dictionary.pop(key)
    return a_dictionary
