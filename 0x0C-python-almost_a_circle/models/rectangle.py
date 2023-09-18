#!/usr/bin/python3
"""
    this code imports and creates a class
"""
from .base import Base
"""
    this imports base from the class Base in the same directory
"""


class Rectangle(Base):
    """
        this is a class  Rectangle which inherits Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            this is a class constructor
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
            to retrive width in this case
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
            to set the width in this case
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """
            this is used ti retrive the height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
            this is used to set height
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """
            used to retrive x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
            used to set x
        """
        if not isinstance(x, int):
            raise TypeError("x must be a integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """
            used to retrive y
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
            used to set y
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
            used to calculate the area
        """
        return self.__width * self.__height

    def display(self):
        """
            used for display in this case # in terms of rectangle
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
            provides a human readable and informative string representation of an object
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """
        checks the number of the argument passed
        """
        if args:
            num_args = len(args)

            if num_args >= 1:
                self.id = args[0]
            if num_args >= 2:
                self.width = args[1]
            if num_args >= 3:
                self.height = args[2]
            if num_args >= 4:
                self.x = args[3]
            if num_args >= 5:
                self.y = args[4]
        if not args and kwargs:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """
             returns a dictionary representation of the rectangle object
        """
        return { 'id':self.id, 'width':self.width, 'height':self.height, 'x':self.x, 'y':self.y}


