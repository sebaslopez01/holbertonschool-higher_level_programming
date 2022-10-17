#!/usr/bin/python3

"""

This modules defines a Square class

"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A Square class
    """

    def __init__(self, size: int, x=0, y=0, id=None):
        """ __init__ method.

        Initialization method

        Args:
            size (:obj:`int`): Size of the square
            x (:obj:`int`, optional): X position
            y (:obj:`int`, optional): Y position
            id (:obj:`int`): id of the instance
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value: int):
        self.width = value
        self.height = value

    def __str__(self):
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'
