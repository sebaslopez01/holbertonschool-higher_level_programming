#!/usr/bin/python3


"""

This module defines a Rectangle class

"""


class Rectangle:
    """ Rectangle Class.

    A basic Rectangle class

    """

    def __init__(self, width=0, height=0):
        """ __init__ method.

        Initialization method

        Args:
            width (:obj:`int`, optional): Width of the rectangle
            height (:obj:`int`, optional): Height of the rectangle
        """
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ :obj:`int` Retrieves the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value: int):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """ :obj:`int` Retrieves the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value: int):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        """Area method to get the area of the rectangle

        Returns:
            The area of the rectangle

        """
        return self.width * self.height

    def perimeter(self):
        """Perimeter method to get the perimeter of the rectangle

        Returns:
            The perimeter of the rectangle

        """
        if self.width == 0 or self.height == 0:
            return 0

        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        new_str = ''

        if self.height == 0 or self.width == 0:
            return new_str

        for i in range(self.height):
            new_str += '#' * self.width
            if i < self.height - 1:
                new_str += '\n'

        return new_str
