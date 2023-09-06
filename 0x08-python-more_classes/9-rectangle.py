#!/usr/bin/python3
"""
this module defines the square class.
"""


class Rectangle:
    """
    this represents a rectangle

    Attributes:
        width and height under two different proprty
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @classmethod
    def square(cls, size=0):
        """
        square class method in the rectangle
        """
        return cls(size, size)

    @property
    def width(self):
        """
        retrieve the width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the size
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        retrieves the height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        returns the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        returns the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        to print # in number of width and height
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for i in range(self.__height):
            rectangle_str += str(self.print_symbol) * self.__width
            if i != self.__height - 1:
                rectangle_str += "\n"
        return rectangle_str

    def __repr__(self):
        """
        returns the string representation
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __eq__(self, other):
        """
        compares two instances of the class
        """
        if isinstance(other, Rectangle):
            return (self.__width == other.width and
                    self.__height == other.height)
        return False

    def __del__(self):
        """
        when a class deleted used to impelemnt it
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        takes two arguments rect_1 and rect_2 instances
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2
