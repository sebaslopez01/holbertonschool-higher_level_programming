#!/usr/bin/python3

"""

This module defines a MyInt class

"""


class MyInt(int):
    """
    MyInt Class
    """

    def __eq__(self, other: int):
        return self != other

    def __ne__(self, other: int):
        return self == other
