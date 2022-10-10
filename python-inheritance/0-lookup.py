#!/usr/bin/python3


def lookup(obj: object):
    """ Get a list of available attributes and methods of
    an object

    Args: 
        obj (:obj:`object`): Object to get the attributes

    Returns:
        A list of attributes and methods
    """
    return dir(obj)
