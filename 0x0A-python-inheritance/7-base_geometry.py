#!/usr/bin/python3
"""BaseGeometry
"""


class BaseGeometry:
    """BaseGeometry class
    """

    def area(self):
        """Area function not yet implemented
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer validator

        Args:
            name (str): name is always a string
            value (int): value is always an integer

        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
