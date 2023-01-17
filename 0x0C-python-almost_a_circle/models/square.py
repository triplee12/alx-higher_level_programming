#!/usr/bin/python3
"""Square model"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        Rectangle.__init__(self, size, size, x, y, id)

    @property
    def size(self):
        """Get size"""

        return self.width

    @size.setter
    def size(self, value):
        """size setter needs to be an int"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """Returns formatted information display"""

        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x, self.y,
                                             self.size)

    def update(self, *args, **kwargs):
        """Update square attributes"""
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
        elif len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            print()

    def to_dictionary(self):
        """Returns a dict representation"""

        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
