#!/usr/bin/python3

""" Square class definition

This module defines a Square class

"""


class Square:
    """ Square class.

    Square class definition

    Attributes:
        __size (int): Size of the square

    """

    def __init__(self, size=0):
        """ __init__ method.

        Initialization method

        Args:
            size (:obj:`int`, optional): Size of the square
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
