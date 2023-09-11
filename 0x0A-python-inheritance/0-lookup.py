#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of available attributes and methods of an objects.

    Args:
        obj (objects): The objects for which you want to lookup

    Returns:
        list:A list of strings representing the attributes
    """
    return dir(obj)
