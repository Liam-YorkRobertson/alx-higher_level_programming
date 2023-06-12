#!/usr/bin/python3
"""
Defines inherited class-checking function.
"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited from class.

    Args:
        obj: Object to check.
        a_class: Class to compare against.

    Returns:
        True if object is instance of class that inherited; otherwise False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return (True)
    return (False)
