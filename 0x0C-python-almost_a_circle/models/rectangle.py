#!/usr/bin/python3
from models.base import Base
"""
Defines Rectangle class.
"""


class Rectangle(Base):
    """
    Class Rectangle that inherits from class Base.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Iniitializes a Rectangle instance.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)  # from Base (parent)

    @property
    def width(self):
        """
        Getter for width.
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Setter for width.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for height.
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Setter for height.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter for x.
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """
        Setter for x.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter for y.
        """
        return (self.__width)

    @y.setter
    def y(self, value):
        """
        Setter for y.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Returns the area of the Rectangle instance.
        """
        return (self.__width * self.__height)

    def display(self):
        """
        Returns a visual Rectangle made of #'s of the Rectangle instance.
        """
        for _ in range(self.__height):  # _ loops indefinitely until specific
            print("#" * self.__width)  # number of times
