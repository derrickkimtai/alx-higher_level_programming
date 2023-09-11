#!/usr/bin/python3
"""
checks if the calss was inherited with is the objects and the methods
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the objects is an instance of or if
    is an instance of a class

    Args:
        obj (object):the object to check
        a_class: class to compare
    Retruns:
    true or false after cheking
    """
    return isinstance(obj, a_class)
