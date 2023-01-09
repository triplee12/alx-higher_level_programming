#!/usr/bin/python3
"""Rectangle inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inherits from BaseGeometry

    Attributes:
        width (int): the rectangle width
        height (int): the rectangle height

    """

    def __init__(self, width, height):
        """Instantiate with width and height

        Args:
            width (int): given width of the rectangle
            height (int): given height of the rectangle

        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
