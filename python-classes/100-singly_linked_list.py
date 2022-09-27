#!/usr/bin/python3

""" Node class and SinglyLinkedList class definition

This module defines a Node class and a SinglyLinkedList class

"""


class Node:
    """ Node class.

    Node class definition

    Attributes:
        __data (int): Data of the node
        __next_node (Node): Next node to point

    """

    def __init__(self, data: int, next_node=None):
        """ __init__ method.

        Initialization method

        Args:
            data (:obj:`int`): Data of the node
            next_node (:obj:`Node`, optional)
        """
        if not isinstance(data, int):
            raise TypeError('data must be an integer')

        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError('next_node must be a Node object')

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ :obj:`int` Retrieves the data of the node
        """
        return self.__data

    @data.setter
    def data(self, value: int):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')

        self.__data = value

    @property
    def next_node(self):
        """ :obj:`Node` Retrieves the next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError('next_node must be a Node object')

        self.__next_node = value


class SinglyLinkedList:
    """ Node class.

    Node class definition

    Attributes:
        __head (Node): Head node

    """

    def __init__(self):
        """ __init__ method.

        Initialization method

        """
        self.__head = None

    def sorted_insert(self, value: int):
        """Inserts a new Node into the correct sorted position

        Args:
            value (:obj:`int`): Node to insert

        """
        if self.__head is None:
            self.__head = Node(value)
            return

        current = self.__head

        while current:
            if value < current.data:
                self.__head = Node(value, current)
                return
            elif value >= current.data and current.next_node is None:
                current.next_node = Node(value)
                return
            elif value >= current.data and value <= current.next_node.data:
                current.next_node = Node(value, current.next_node)
                return

            current = current.next_node

    def __str__(self):
        new_string = ''

        current = self.__head

        while current:
            new_string += str(current.data)
            if current.next_node is not None:
                new_string += '\n'

            current = current.next_node

        return new_string
