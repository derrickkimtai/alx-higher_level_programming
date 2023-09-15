import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_rectangle_init(self):
        r = Rectangle(10, 20, 30, 40, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 30)
        self.assertEqual(r.y, 40)
        self.assertEqual(r.id, 1)

    if __name__ == '__main__':
        unittest.main()
