#!/usr/bin/python3
"""
this just a python code of class base and id
"""


class Base:
    """
        this is a class with base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            manages id attribute in all the clasess I will create
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
