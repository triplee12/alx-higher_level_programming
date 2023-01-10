#!/usr/bin/python3
"""save_to_json_file module"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using a json representation

    Args:
        my_obj (dict): dictionary to write
        filename (file): file name to write the object

    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
