#!/usr/bin/python3
"""append_write module"""


def append_write(filename="", text=""):
    """Append string at the end of file and returns the number
    of characters added

    Args:
        filename (str): file name to append a string
        text (str): string to append to a file

    """
    with open(filename, "a", encoding="utf-8") as f:
        myfile = f.write(text)
        return myfile
