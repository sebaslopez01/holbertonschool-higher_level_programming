#!/usr/bin/python3

"""

This module defines a MyInt class

"""


class MyInt(int):
    """
    MyInt Class
    """

    def __eq__(self, other: int):
        res = super().__eq__(other)
        return not res

    def __ne__(self, other: int):
        res = super().__ne__(other)
        return not res
