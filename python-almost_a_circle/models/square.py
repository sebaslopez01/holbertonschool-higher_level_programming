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

    def update(self, *args, **kwargs):
        """
        Updates the values of the Rectangle

        Args:
            args (:obj:`tuple`): Arguments
        """
        if len(args) > 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                return

        self.id = kwargs.get('id', self.id)
        self.width = kwargs.get('size', self.width)
        self.height = kwargs.get('size', self.height)
        self.x = kwargs.get('x', self.x)
        self.y = kwargs.get('y', self.y)

    def __str__(self):
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'
