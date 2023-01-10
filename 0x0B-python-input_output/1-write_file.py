#!/usr/bin/python3
"""write_file module"""


def write_file(filename="", text=""):
    """Write string to a text file and returns the number
    of characters written

    Args:
        filename (str): file name of the file to write
        text (str): the string to write in the file

    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        line_num = 0

        for line in f:
            line_num += 1

        return line_num
