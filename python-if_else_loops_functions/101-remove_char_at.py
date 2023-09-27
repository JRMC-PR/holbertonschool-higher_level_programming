#!/usr/bin/python3
def remove_char_at(str, n):
    # TODO: Remove the character at the position n of a string.
    # ? str: string to copy from
    # ? n: position of the character to remove
    # Return: the copy of the string without the character at the position n.
    if n < 0:
        return str
    return str[:n] + str[n + 1:]
