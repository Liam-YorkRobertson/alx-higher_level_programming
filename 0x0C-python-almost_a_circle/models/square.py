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

        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    def update(self, *args, **kwargs):
        """
        Updates Square using args.
        """

        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        elif kwargs:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """
        Returns dictionary representation of Square.
        """

        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
