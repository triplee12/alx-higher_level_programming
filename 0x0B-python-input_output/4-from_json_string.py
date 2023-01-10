#!/usr/bin/python3
"""from_json_string module"""
import json


def from_json_string(my_str):
    """Returns an object represented by a json string

    Args:
        my_str (str): json file

    """
    my_obj = json.loads(my_str)
    return my_obj
