#!/usr/bin/python3
"""Square inherits data from Rectangle"""
Rectangle = __import__("9-rectangle.py").Rectangle


class Square(Rectangle):
    """Square inherits data from Rectangle

    Attributes:
        size (int): size must be integer
    """

    def __init__(self, size):
        """Initializer of rectangle

        args:
            size (int): size must be integer
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the Square area"""
        return self.__size**2
