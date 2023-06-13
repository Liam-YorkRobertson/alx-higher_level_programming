#!/usr/bin/python3
"""
Define a Rectangle (child of BaseGeometry) subclass class Square (grandchild)
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square.
    """
    def __init__(self, size):
        self.integer_validator = ("size", size)
        self.__size = size
        super().__init__(size, size)
