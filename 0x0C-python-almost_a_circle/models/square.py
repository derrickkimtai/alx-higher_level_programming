#!/usr/bin/bash
from .rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """
            call the super constructor with id , x, y, width, and height
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
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
        if args:
            attribute = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attribute):
                    setattr(self, attribute[i], arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
    def __str__(self):
        """
            override the __str__ method to return a string representation
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
