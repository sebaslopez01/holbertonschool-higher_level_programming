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

    @property
    def size(self):
        """ :obj:`int` Retrieves the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value: int):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def area(self):
        """Area method to get the area of the square

        Returns:
            The are of the square

        """
        return self.__size ** 2

    def __eq__(self, other):
        return self.size == other.size

    def __ne__(self, other):
        return self.size != other.size

    def __gt__(self, other):
        return self.size > other.size

    def __ge__(self, other):
        return self.size >= other.size

    def __lt__(self, other):
        return self.size < other.size

    def __le__(self, other):
        return self.size <= other.size
