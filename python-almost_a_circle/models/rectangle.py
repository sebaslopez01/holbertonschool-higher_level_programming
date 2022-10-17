#!/usr/bin/python3

"""

This modules defines a Rectangle class

"""

from models.base import Base


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
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value: int):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value: int):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')

        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value: int):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')

        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')

        self.__y = value

    def area(self):
        """Area method to get the area of the rectangle

        Returns:
            The area of the rectangle

        """
        return self.width * self.height

    def display(self):
        """
        Prints the Rectangle with the character #
        """
        for _ in range(self.y):
            print()

        for _ in range(self.height):
            print(' ' * self.x, sep='', end='')
            print('#' * self.width, sep='')

    def __str__(self):
        return f'[Rectangle] ({self.id}) {self.x}/{self.y} \
- {self.width}/{self.height}'
