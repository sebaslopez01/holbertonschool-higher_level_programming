#!/usr/bin/python3

"""

This module defines a Rectangle class

"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    A Rectangle class
    """

    def __init__(self, width: int, height: int):
        """ __init__ method.

        Initialization method

        Args:
            width (:obj:`int`): Width of the rectangle
            height (:obj:`int`): Height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
