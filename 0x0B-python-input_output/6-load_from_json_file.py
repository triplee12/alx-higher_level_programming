#!/usr/bin/python3
"""load_from_json_file module"""
import json


def load_from_json_file(filename):
    """Creates an object from a json file

    Args:
        filename (file): file name to write object from

    """
    with open(filename, "w", encoding="utf-8") as f:
        json.load(f)
