#!/usr/bin/python3
"""read_file"""


def read_file(filename=""):
    """Read file and prints it to stdout

    Args:
        filename (str): file name to read
    """
    with open(filename, "r", encoding="utf-8") as f:
        myfile = f.read()
        print(myfile, end="")
