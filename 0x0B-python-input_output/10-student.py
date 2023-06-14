#!/usr/bin/python3
"""
Defines class Student.
"""


class Student:
    """
    Represent a student.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name  # str
        self.last_name = last_name  # str
        self.age = age  # int

    def to_json(self, attrs=None):
        """
        Get a dictionary representation of the student.
        """

        if attrs is None:
            return (self.__dict__)
        return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

