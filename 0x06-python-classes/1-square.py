#!/usr/bin/python3
"""
This module defines the square class.

This module contains the definition of the square class.
"""


class Square:
    """
    This class represents a square.

    Attributes:
            __size (int): The size of the square's sides.
    Methods:
            __init__(self, size):Intializes a new square instance.
            area : calculates the area of the square.
    """
    def __init__(self, size):
        """
        calculates the area of the square.

        Returns:
            int: The area of the square.

        """
        self.__size = size
