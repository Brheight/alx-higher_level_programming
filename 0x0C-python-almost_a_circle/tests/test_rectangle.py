import unittest
from unittest.mock import patch
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_init(self):
        r = Rectangle(10, 20)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_init_custom_id(self):
        r = Rectangle(10, 20, 5, 10, 7)
        self.assertEqual(r.id, 7)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 10)

    def test_validate_non_negative_int_valid(self):
        r = Rectangle(10, 20)
        r.validate_non_negative_int("test", 5)

    def test_validate_non_negative_int_negative(self):
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            r.validate_non_negative_int("test", -5)

    def test_validate_non_negative_int_non_integer(self):
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            r.validate_non_negative_int("test", "string")

    def test_area(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_display(self):
        r = Rectangle(3, 2, 1, 0)
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            r.display()
            output = mock_stdout.getvalue()
            self.assertEqual(output, "\n ###\n ###\n")

    def test_str(self):
        r = Rectangle(10, 20, 5, 10, 7)
        self.assertEqual(str(r), "[Rectangle] (7) 5/10 - 10/20")

    def test_to_dictionary(self):
        r = Rectangle(10, 20, 5, 10, 7)
        self.assertEqual(r.to_dictionary(), {'id': 7, 'width': 10, 'height': 20, 'x': 5, 'y': 10})

    def test_update_args(self):
        r = Rectangle(10, 20, 5, 10, 7)
        r.update(1, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (1) 3/4 - 2/5")

    def test_update_kwargs(self):
        r = Rectangle(10, 20, 5, 10, 7)
        r.update(width=2, height=3, x=4, y=5, id=1)
        self.assertEqual(str(r), "[Rectangle] (1) 4/5 - 2/3")

    def test_negative_dimensions(self):
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2, 3, 4)
        with self.assertRaises(ValueError):
            r = Rectangle(1, -2, 3, 4)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, -3, 4)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 3, -4)

    def test_zero_dimensions(self):
        r = Rectangle(0, 0, 0, 0)
        self.assertEqual(r.width, 0)
        self.assertEqual(r.height, 0)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_update_with_invalid_values(self):
        r = Rectangle(1, 1, 1, 1)
        with self.assertRaises(ValueError):
            r.update(width=-1)
        with self.assertRaises(ValueError):
            r.update(height=-2)
        with self.assertRaises(ValueError):
            r.update(x=-3)
        with self.assertRaises(ValueError):
            r.update(y=-4)

    def test_display_empty_rectangle(self):
        r = Rectangle(0, 0, 2, 2)
        with self.assertRaises(ValueError):
            r.display()

    def test_large_values(self):
        r = Rectangle(999999, 888888, 777777, 666666)
        self.assertEqual(r.width, 999999)
        self.assertEqual(r.height, 888888)
        self.assertEqual(r.x, 777777)
        self.assertEqual(r.y, 666666)

    def test_overlap_detection(self):
        r1 = Rectangle(1, 1, 1, 1)
        r2 = Rectangle(1, 1, 2, 2)
        self.assertTrue(r1.overlaps(r2))

if __name__ == "__main__":
    unittest.main()
