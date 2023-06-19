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

        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns dictionary representation of json_string.
        """

        if json_string is None or json_string == []:
            return ([])
        else:
            return json.loads(json_string)

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

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.
        """

        if cls.__name__ == "Rectangle":
            new_inst  = cls(1, 1)
        elif cls.__name__ == "Square":
            new_inst = cls(1)

        new_inst.update(**dictionary)

        return (new_inst)
