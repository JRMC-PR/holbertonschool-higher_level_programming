#!/usr/bin/python3
""" prints a text with 2 new lines after each of these characters: ., ?and:"""


def text_indentation(text):
    """
    >>> text_indentation("")

    >>> text_indentation('')

    >>> text_indentation("?")
    ?
    <BLANKLINE>
    >>> text_indentation(":")
    :
    <BLANKLINE>
    >>> text_indentation(".")
    .
    <BLANKLINE>
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.strip()
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(text[i])
            print()
            if i != len(text) - 1:
                if text[i + 1] == ' ':
                    i += 1
        else:
            print(text[i], end="")
