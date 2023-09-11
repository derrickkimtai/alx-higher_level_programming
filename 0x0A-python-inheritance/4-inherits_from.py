#!/usr/bin/python3
"""
the module checks if the objects is an instance of a class that inherited
"""


def inherits_from(obj, a_class):
    """
    Return True if the objets is an instance of a class
    from the specified class; otherwise False.

    Args:
        obj (object): the objets to check
        a_class (class): the class to compare against
    Returns:
        bool: True if the objects 
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
