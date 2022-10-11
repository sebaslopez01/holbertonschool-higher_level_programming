#!/usr/bin/python3

"""

This module defines a Student class

"""


class Student:
    """
    A Student class
    """

    def __init__(self, first_name: str, last_name: str, age: int):
        """ __init__ method.

        Initialization method

        Args:
            first_name (:obj:`str`): First name
            last_name (:obj:`str`): Last name
            age (:obj:`int`): Age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance

        Args:
            attrs (:obj:`list`, optional): A list of string

        Returns:
            A dictionary representation of a Student instance
        """
        new_dict = {}

        if attrs is not None:
            for attr in attrs:
                if attr in self.__dict__:
                    new_dict[attr] = self.__dict__.get(attr)
        else:
            return self.__dict__

        return new_dict

    def reload_from_json(self, json: dict):
        """
        Replaces all attributes of the Student instance

        Args:
            json (:obj:`dict`): Dictionary
        """
        for key, value in json.items():
            self.__dict__[key] = value
