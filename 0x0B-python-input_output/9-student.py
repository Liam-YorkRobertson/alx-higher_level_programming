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

    def to_json(self):
        return (self.__dict__)
