#!/usr/bin/python3
"""
this use a class of rectangle by importation
"""
from .rectangle import Rectangle
"""
imports the class Rectangle
"""

class Square(Rectangle):
    """
        this is a class Rectangle with many terms
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            call the super constructor with id , x, y, width, and height
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
            retrievs thesize
        """
        return self.width
    @size.setter
    def size(self, value):
        """
            used to set the size value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
         it used to update
        """
        if args:
            attribute = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attribute):
                    setattr(self, attribute[i], arg)
        else:
            for key, value in kwargs.items():
                if key in ("id", "size", "x", "y"):
                    setattr(self, key, value)
    def __str__(self):
        """
            override the __str__ method to return a string representation
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def to_dictionary(self):
        """
            Returns a dictionary representation of the rectangle object
        """
        return {'id': self.id, 'size':self.size, 'x':self.x, 'y':self.y}
