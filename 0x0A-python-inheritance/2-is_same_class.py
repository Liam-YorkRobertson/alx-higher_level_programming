#!/usr/bin/python3
"""
Defines a function that checks class.
"""


def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of specified class.

    Args:
        obj: An object to check.
        a_class: A class to compare against.

    Returns:
        True if the object is exactly an instance; otherwise, False.
    """

    if type(obj) == a_class:
        return (True)
    else:
        return (False)
