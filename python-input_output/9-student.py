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

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance

        Returns:
            A dictionary representation of a Student instance
        """
        return self.__dict__
