#!/usr/bin/python3

"""

This modules defines a Base class

"""


class Base:
    """
    Base class

    Attributes:
        __nb_objects (:obj:`int`): Counter of objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ __init__ method.

        Initialization method

        Args:
            id (:obj:`int`): id of the instance
        """
        if id is not None:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects
