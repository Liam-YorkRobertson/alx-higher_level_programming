#!/usr/bin/python3
"""
Defines a file writing function.
"""


def write_file(filename="", text=""):
    """
    Write a string to a utf8 file.
    """

    with open(filename, "w", encoding="utf-8") as file:
        return (file.write(text))
