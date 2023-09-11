#!/usr/bin/python3
"""
this module has two  class basegometry and rectangle
"""


class BaseGeometry:
    """
    calculates and returns the area of the geometric shape

    it checks some errors and raises the instanly whatsoever the case
    """
    def area(self):
        """
        it raises an error to the area methof of instastiation
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate an integer value

        Parameters:
            name (str):the name of the value being validated.
            value (int): the value to be validated.

        Raises:
        TypeError: if the value is not an integer
        ValueError: If the value is less then
        """
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Initializes a rectangle object with width and height

    Parameters:
        width (int): the width of the rectangle.
        haight (int): the height of the rectangle.
    raises:
         the same error as the previous ones above mentioned
    """
    def __init__(self, width, height):
        """
        it has two attributes with should not be positives

        takes two parameters
        """
        self.__width = None
        self.__height = None
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        finds thr area by multiplication
        """
        return self.__width * self.__height

    def __str__(self):
        """
        used in print function used for a more readble format
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        """
        returns a string representation that is more readble
        """
        return self.__str__()
