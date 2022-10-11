#!/usr/bin/python3

"""

This module defines a MyList class

"""


class MyList(list):
    """
    A MyList class
    """

    def print_sorted(self):
        """
        Prints the list, but sorted in ascending order

        Returns:
            A new list with the sorted values
        """
        new_list = sorted(self)
        print(new_list)

        return new_list
