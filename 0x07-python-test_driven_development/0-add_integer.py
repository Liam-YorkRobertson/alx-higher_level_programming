#!/usr/bin/python3
# 0-add_integer.py
"""

Defines an integer addition function.

"""


def add_integer(a, b=98):
    """ Args: a (int): The first integer and b (int).
        Returns (int) The sum of a and b.
        Raises TypeError If a or b is not an integer or float."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    return (int(a) + int(b))
