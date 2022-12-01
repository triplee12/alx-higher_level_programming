#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    """Print the sum of all arguments.
    Follows by newline.
    """
    result = 0
    if len(argv) == 1:
        print(result)
    else:
        for i in range(len(argv) - 1):
            result += int(argv[i + 1])
        print(result)
