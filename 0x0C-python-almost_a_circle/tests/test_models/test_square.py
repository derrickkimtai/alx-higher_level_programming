import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_square_init(self):
        s = Square(5, 10, 15, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 10)
        self.assertEqual(s.y, 15)
        self.assertEqual(s.id, 1)

    def test_size_setter(self):
        s = Square(5)
        s.size = 7
        self.assertEqual(s.size, 7)

    def test_update_with_args(self):
        s = Square(1)
        s.update(10, 20, 30, 40)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 20)
        self.assertEqual(s.x, 30)
        self.assertEqual(s.y, 40)

    def test_update_with_kwargs(self):
        s = Square(1)
        s.update(id=10, size=20, x=30, y=40)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 20)
        self.assertEqual(s.x, 30)
        self.assertEqual(s.y, 40)

    def test_update_with_mixed_args_and_kwargs(self):
        s = Square(1)
        s.update(10, 20, x=30, y=40)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 20)
        self.assertEqual(s.x, 30)
        self.assertEqual(s.y, 40)

    def test_update_with_empty_args_and_kwargs(self):
        s = Square(1)
        s.update()
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_str_method(self):
        s = Square(5, 10, 15, 1)
        self.assertEqual(str(s), "[Square] (1) 10/15 - 5")

    def test_to_dictionary_method(self):
        s = Square(5, 10, 15, 1)
        expected_dict = {'id': 1, 'size': 5, 'x': 10, 'y': 15}
        self.assertEqual(s.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()

