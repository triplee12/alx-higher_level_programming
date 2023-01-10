#!/usr/bin/python3
"""to_json_string module"""
import json


def to_json_string(my_obj):
    """Returns json representation of an object

    Args:
        my_obj (dict): dictionary file to serialize

    """
    my_json_file = json.dumps(my_obj)
    return my_json_file
