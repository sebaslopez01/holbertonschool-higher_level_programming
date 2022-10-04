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
