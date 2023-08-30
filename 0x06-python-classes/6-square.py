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
    def __init__(self, size=0, position=(0, 0)):
        """
        intializes a new square instance.

        Args:
            size(int, optional): the size of the  square's side
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        retrieve the position
        """
        return self.__position

    @position.setter
    def positon(self, value):
        """
        set the position attribute
        """
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) and num > 0 for num in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        calculates the area
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints the square using the # character.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print("" * self.__position[0] + "#" * self.__size)
