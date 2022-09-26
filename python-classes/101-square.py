#!/usr/bin/python3

""" Square class definition

This module defines a Square class

"""


class Square:
    """ Square class.

    Square class definition

    Attributes:
        __size (int): Size of the square
        __position (tuple): Position of the square

    """

    def __init__(self, size=0, position=(0, 0)):
        """ __init__ method.

        Initialization method

        Args:
            size (:obj:`int`, optional): Size of the square
            position (:obj:`tuple` of :obj:`int`, optional): Position
            of the square
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        if not isinstance(position, tuple) or len(position) != 2 \
                or not isinstance(position[0], int) \
                or not isinstance(position[1], int) \
                or position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ :obj:`tuple` of :obj:`int` Retrieves the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value: tuple):
        if not isinstance(value, tuple) or len(value) != 2 \
                or not isinstance(value[0], int) \
                or not isinstance(value[1], int) \
                or value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = value

    def area(self):
        """Area method to get the area of the square

        Returns:
            The are of the square

        """
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.position[1]):
            print()

        for _ in range(self.__size):
            print(' ' * self.__position[0], sep='', end='')
            print('#' * self.__size, sep='')

    def __str__(self):
        if self.__size == 0:
            return ''

        new_string = ''

        for _ in range(self.position[1]):
            new_string += '\n'

        for _ in range(self.__size):
            new_string += ' ' * self.__position[0]
            new_string += '#' * self.__size
            new_string += '\n'

        return new_string
