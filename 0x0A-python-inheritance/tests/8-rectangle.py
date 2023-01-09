#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry.py').BaseGeometry

"""Rectangle
"""


class Rectangle(BaseGeometry):
    """Rectangle class inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """Instantiate with width and height

        Args:
            width (int): given width of the rectangle
            height (int): given height of the rectangle

        """

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
