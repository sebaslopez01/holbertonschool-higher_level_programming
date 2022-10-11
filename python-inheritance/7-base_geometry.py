#!/usr/bin/python3

"""

This module defines a BaseGeometry class

"""


class BaseGeometry:
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
        if not isinstance(value, int):
            raise TypeError(f'{value} must be an integer')
        if value <= 0:
            raise ValueError(f'{value} must be greater than')