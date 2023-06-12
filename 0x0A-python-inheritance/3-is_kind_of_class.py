#!/usr/bin/python3
"""
Defines a class and inherited class-checking function.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or inherited from class.

    Args:
        obj: Object to check.
        a_class: Class to compare against.

    Returns:
        True if the object is an instance of, or inherited; False otherwise.
    """

    if isinstance(obj, a_class):
        return (True)
    return (False)
