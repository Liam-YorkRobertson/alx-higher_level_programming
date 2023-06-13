#!/usr/bin/python3
"""
Defines a function that writes JSON files.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a textfile using JSON representation.
    """

    with open(filename, "w") as file:
        json.dump(my_obj, file)
