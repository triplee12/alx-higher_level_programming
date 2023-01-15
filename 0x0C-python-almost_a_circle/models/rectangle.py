#!/usr/bin/python3
"""Rectangle class that inherits Base class"""
from base import Base


class Rectangle(Base):
    """Rectangle class that inherits Base class

    Attributes:
        width (int): width of the rectagle
        height (int): height of the rectangle
        x (int): x axis
        y (int): y axis
        id (int or None): id of the rectangle

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        """Width of the rectangle

        Args:
            w (int): the width

        """
        self.__width = w

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        """Height of the rectangle

        Args:
            h (int): the height

        """
        self.__height = h

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x_axis):
        """X axis of the rectangle

        Args:
            x_axis (int): the x axis

        """
        self.__x = x_axis

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y_axis):
        """Y axis of the rectangle

        Args:
            y_axis (int): the y axis

        """
        self.__y = y_axis
