#!/usr/bin/python3

"""

This modules defines a Rectangle class

"""

from base import Base


class Rectangle(Base):
    """
    A Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ __init__ method.

        Initialization method

        Args:
            width (:obj:`int`): Width of the rectangle
            height (:obj:`int`): Height of the rectangle
            x (:obj:`int`, optional): X position
            y (:obj:`int`, optional): Y position
            id (:obj:`int`): id of the instance
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value: int):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value: int):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value: int):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value


r1 = Rectangle(10, 2)
print(r1.id)

r2 = Rectangle(2, 10)
print(r2.id)

r3 = Rectangle(10, 2, 0, 0, 12)
print(r3.id)
