#!/usr/bin/python3
"""
this mmodule checks if the object is exactly an instance of the class
"""


def is_same_class(obj, a_class):
    """
    checks if the object is exactly an instance of the specified class
    """
    return type(obj) is a_class
