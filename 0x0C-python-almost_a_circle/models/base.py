#!/usr/bin/python3
"""
Defines Base function.
"""


class Base:
    """
    Base model for all other classes (Rectangle and Square).
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
