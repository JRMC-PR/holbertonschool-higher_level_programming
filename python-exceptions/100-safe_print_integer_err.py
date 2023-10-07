#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, Exception):
        # the next line prints the error to stderr
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False
