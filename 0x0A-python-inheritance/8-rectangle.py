#!/usr/bin/python3
"""
Defines a subclass Rectangel that inherits from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents Rectangle subclass of BaseGeometry
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator = ("width", width)
        self.integer_validator = ("height", height)
