import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os

class TestBase(unittest.TestCase):
    def test_id_assignment_with_arguments(self):
        obj = Base(10)
        self.assertEqual(obj.id, 10)

    def test_id_assignment_without_arguments(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

class TestRectangle(unittest.TestCase):
    def test_width_and_height(self):
        r = Rectangle(10, 20)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)

    def test_area(self):
        r = Rectangle(5, 6)
        self.assertEqual(r.area(), 30)

class TestSquare(unittest.TestCase):
    def test_size(self):
        s = Square(7)
        self.assertEqual(s.size, 7)

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

if __name__ == '__main__':
    unittest.main()

