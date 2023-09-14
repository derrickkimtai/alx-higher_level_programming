import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_id_assignment_with_arguments(self):
        obj = Base(10)
        self.assertEqual(obj.id, 10)

    def test_id_assigment_without_arguments(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)


    if __name__ == '__main__':
        unittest.main()
