import unittest
from unittest.mock import patch
from models.base import Base


class TestBase(unittest.TestCase):

    def test_init(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_init_custom_id(self):
        b = Base(5)
        self.assertEqual(b.id, 5)

    def test_init_incremental_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_validate_non_negative_int_valid(self):
        Base.validate_non_negative_int("test", 10)

    def test_validate_non_negative_int_negative(self):
        with self.assertRaises(ValueError):
            Base.validate_non_negative_int("test", -5)

    def test_validate_non_negative_int_non_integer(self):
        with self.assertRaises(ValueError):
            Base.validate_non_negative_int("test", "string")

    def test_to_json_string(self):
        b = Base()
        self.assertEqual(Base.to_json_string([b.to_dictionary()]), '[{"id": 1}]')

    def test_to_json_string_empty_list(self):
        self.assertEqual(Base.to_json_string([]), '[]')

    def test_from_json_string(self):
        json_string = '[{"id": 1}]'
        self.assertEqual(Base.from_json_string(json_string), [{"id": 1}])

    def test_from_json_string_empty_string(self):
        self.assertEqual(Base.from_json_string(''), [])

    @patch("builtins.open", create=True)
    def test_save_to_file(self, mock_open):
        b = Base()
        b.save_to_file([b])
        mock_open.assert_called_with('Base.json', 'w', encoding='utf-8')

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_load_from_file_file_not_found(self, mock_open):
        r = Base.load_from_file()
        self.assertEqual(r, [])

    def test_create(self):
        b = Base()
        r = b.create()
        self.assertIsInstance(r, Base)

    @patch("builtins.open", create=True)
    def test_save_to_file_csv(self, mock_open):
        b = Base()
        b.save_to_file_csv([b])
        mock_open.assert_called_with('Base.csv', 'w', newline='', encoding='utf-8')

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_load_from_file_csv_file_not_found(self, mock_open):
        r = Base.load_from_file_csv()
        self.assertEqual(r, [])

    def test_draw(self):
        pass

if __name__ == '__main__':
    unittest.main()
