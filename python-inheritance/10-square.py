#!/usr/bin/python3

"""

This module defines a Rectangle class

"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    A Square class
    """

    def __init__(self, size: int):
        """ __init__ method.

        Initialization method

        Args:
            size (:obj:`int`): Size of the square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Gets the area of the square
        """
        return self.__size * self.__size
