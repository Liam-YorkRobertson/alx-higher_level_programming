#!/usr/bin/python3
"""
Defines a test file-reading function.
"""


def read_file(filename=""):
    """
    Print contents of a utf-8 test file
    """

    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
