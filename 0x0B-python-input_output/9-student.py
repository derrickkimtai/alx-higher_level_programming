#!/usr/bin/python3
"""
defines a json class
"""

class Student:
    def __init__(self, first_name, last_name, age):
        """
        this is just instantiation of attributes
        """
        self.first_name = first_name
        self.first_name = first_name
        self.age = age

def to_json(self):
    """
    functions of the dictionary data structure
    """
    return {
        "first_name": self.first_name,
        "last_name": self.last_name,
        "age": self.age
        }
