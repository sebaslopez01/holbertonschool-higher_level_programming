#!/usr/bin/python3

"""

This module defines a BaseGeometry class and a Rectangle class

"""


class BaseGeometry(type):
    """
    A BaseGeometry class
    """

    def area(self):
        """
        Raises an Exception
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name: str, value: int):
        """
        Validates a value
        """
        if not type(value) is int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')


class Rectangle(BaseGeometry):
    """
    A Rectangle class
    """

    def __init__(self, width: int, height: int):
        """ __init__ method.

        Initialization method

        Args:
            width (:obj:`int`, optional): Width of the rectangle
            height (:obj:`int`, optional): Height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
