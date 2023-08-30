#!/usr/bin/python3
"""
this module defines the square class.
"""


class Square:
    """
    this represents a square.

    Attributes:
            __size(int): The size of the square's sides.
    Methods:
        __init__(self, size=0):Initializes a new square instances
        size(self): Getter method to retrieve
        size(self, value):setter method to set the size attribute.
        area(self): calculates the area
    """
    def __init__(self, size=0):
        """
        intializes a new square instance.

        Args:
            size(int, optional): the size of the  square's side
        """
        self.__size = size

    @property
    def size(self):
        """
        retrieves he size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets the size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__value = value

    def area(self):
        """
        calculates the area
        """
        return self.__size ** 2
