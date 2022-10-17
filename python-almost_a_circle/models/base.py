#!/usr/bin/python3

"""

This modules defines a Base class

"""

import json


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
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Gets the JSON representation of a list of dictionaries

        Returns:
            The JSON representation of a list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'

        return json.dumps(list_dictionaries)
