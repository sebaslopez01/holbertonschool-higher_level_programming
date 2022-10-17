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

        Args:
            list_dictionaries (:obj:`list[dict]`): A list of dictionaries

        Returns:
            The JSON representation of a list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'

        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string: str):
        """
        Gets the list of the JSON string representation json_string

        Args:
            json_string (:obj:`str`): A string representating a list of dicts

        Returns:
            The list of the JSON string representation json_string
        """
        if json_string is None or json_string == '':
            return []

        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file

        Args:
            list_objs (:obj:`list[Base]`): A list of Base objects
        """
        if list_objs is None:
            list_objs = []

        with open(f'{cls.__name__}.json', 'w') as f:
            lst_dict = list(map(lambda x: x.to_dictionary(), list_objs))
            f.write(cls.to_json_string(lst_dict))

    @classmethod
    def create(cls, **dictionary):
        """
        Gets an instance with all attributes already set

        Args:
            dictionary (:obj:`dict`): Dictionary with attributes to set

        Returns:
            An instance with all attributes already set
        """
        new_instance = cls(**dictionary)
        new_instance.update(**dictionary)

        return new_instance
