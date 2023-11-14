import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_create_instance(self):
        s = Square(5, 1, 2, 3)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 3)

    def test_size_property(self):
        s = Square(10)
        self.assertEqual(s.size, 10)
        s.size = 15
        self.assertEqual(s.size, 15)
        self.assertEqual(s.width, 15)
        self.assertEqual(s.height, 15)

    def test_size_validation(self):
        with self.assertRaises(ValueError):
            s = Square(-1)
        with self.assertRaises(ValueError):
            s = Square(0)
        with self.assertRaises(ValueError):
            s = Square(1, -2)
        with self.assertRaises(ValueError):
            s = Square(1, 2, -3)

    def test_to_dictionary(self):
        s = Square(4, 2, 1, 7)
        dictionary = s.to_dictionary()
        self.assertEqual(dictionary, {'id': 7, 'size': 4, 'x': 2, 'y': 1})

    def test_str_representation(self):
        s = Square(3, 1, 2, 5)
        self.assertEqual(str(s), "[Square] (5) 1/2 - 3")

    def test_negative_size(self):
        with self.assertRaises(ValueError):
            s = Square(-5, 1, 2, 3)


if __name__ == '__main__':
    unittest.main()
