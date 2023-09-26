#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        # ord(0 is used to tget the unicode of the character)
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            print("{}".format(chr(ord(str[i]) - 32)), end="")
        else:
            print("{}".format(str[i]), end="")
    print()
