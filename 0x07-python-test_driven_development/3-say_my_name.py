#!/usr/bin/python3
"""
Prints the name in the format "My name is <first name> <last name>".
"""


def say_my_name(first_name, last_name=""):
    """
    Prints name in the format "My name is <first name> <last name>".
    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to an empty string.
    Raises:
        TypeError: If first_name is not a string.
        TypeError: If last_name is provided and not a string.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    full_name = "My name is " + first_name

    if last_name:
        full_name += " " + last_name

    print(full_name)
