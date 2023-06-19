#!/usr/bin/python3
import json
"""
Defines Base function.
"""


class Base:
    """
    Base model for all other classes (Rectangle and Square).
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes Base function.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns json representation of list_dictionaries
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Returns the list of the JSON string representation json_string.
        """

        filename = cls.__name__ + ".json"

        if list_objs is None:
            list_objs = []

        list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dicts)

        with open(filename, 'w') as file:
            file.write(json_string)
