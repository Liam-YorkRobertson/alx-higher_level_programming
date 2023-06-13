#!/usr/bin/python3
"""
Defines a function that read json files
"""
import json


def load_from_json_file(filename):
    """
    Create a python object from a json file.
    """

    with open(filename) as file:
        return (json.load(file))
