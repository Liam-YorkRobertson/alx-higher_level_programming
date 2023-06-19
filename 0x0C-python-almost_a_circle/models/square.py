#!/usr/bin/python3
"""
Defines Square class (inherits from Rectangle).
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a Square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes Square class.
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter for size.
        """

        return (self.width)

    @size.setter
    def size(self, value):
        """
        """

        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns string representation of this Square instance.
        """
        return (f"[square] ({self.id}) {self.x}/{self.y} - {self.width}")
