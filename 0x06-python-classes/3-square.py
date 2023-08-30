#!/usr/bin/python3
"""
This module defines the square class.

This module contains the definition of the square class
"""


class Square:
    """
    This class represents a square a square.

    Attributes:
            __size (int): The size of the square's sides.

    Methods:
        __init__self,size=0): init a new square instance.
    """
    def __init__(self, size=0):
        """
        initializes a new square instance.

        Args:
            size : the size of the size of the square's sides

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
