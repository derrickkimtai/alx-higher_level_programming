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

    def test_width_setters(self):
        r = Rectangle(5, 5)
        r.width = 10
        self.assertEqual(r.width, 10)
    def test_heigth_setters(self):
        r = Rectangle(5, 10)
        r.heigth = 10
        self.assertEqual(r.height, 10)
    def test_x_stters(self):
        r = Rectangle(5, 6)
        r.x = 10
        self.assertEqual(r.x, 10)
    def test_y_setters(self):
        r = Rectangle(6, 5)
        r.y = 60
        self.assertEqual(r.y, 60)

    def test_area(self):
        x = Rectangle(5, 5)
        self.assertEqual(x.area(), 25)
    def test_display(self):
        import io
        import sys

        r = Rectangle(3, 2)
        expected_output = "###\n###\n"

        captured_output = io.StringIO()
        sys.stdout = captured_output

        r.display()

        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), expected_output)

class TestUpdateMethod(unittest.TestCase):
    def test_update_with_args(self):
        r = Rectangle(1, 1)
        r.update(10, 20, 30, 40, 50)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)

    def test_update_with_kwargs(self):
        r = Rectangle(1, 1)
        r.update(id=10, width=20, height=30, x=40, y=50)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y 50)

    def test_update_with_mixed_args_and_kwargs(self):
        r = Rectangle(1, 1)
        r.update(10, width=20, x=40)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height 1)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 0)

    def test_update_with_empty_args_and_kwargs(self):
        r = Rectangle(1, 1)
        r.update()
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    if __name__ == '__main__':
        unittest.main()
