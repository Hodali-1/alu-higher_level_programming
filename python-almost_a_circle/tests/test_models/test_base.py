#!/usr/bin/python3
"""Unit tests for the Base class."""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for id handling and JSON helpers of Base."""

    def test_auto_id(self):
        """Consecutive instances without id get incrementing ids."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_given_id(self):
        """An explicit id is stored unchanged."""
        self.assertEqual(Base(89).id, 89)

    def test_to_json_string_none(self):
        """None serializes to the empty-list string."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """An empty list serializes to the empty-list string."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_value(self):
        """A list of dicts serializes to valid JSON text."""
        s = Base.to_json_string([{"id": 1}])
        self.assertEqual(s, '[{"id": 1}]')

    def test_from_json_string_none(self):
        """None deserializes to an empty list."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_value(self):
        """A JSON list string deserializes to a list of dicts."""
        self.assertEqual(Base.from_json_string('[{"id": 1}]'), [{"id": 1}])

    def test_create_rectangle(self):
        """create() builds a Rectangle equal to the source dictionary."""
        r1 = Rectangle(3, 5, 1, 2, 7)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    def test_save_and_load(self):
        """save_to_file then load_from_file round-trips instances."""
        Square.save_to_file([Square(4, 1, 1, 9)])
        loaded = Square.load_from_file()
        self.assertEqual(loaded[0].to_dictionary()["size"], 4)

    def test_load_missing_file(self):
        """load_from_file returns [] when the file is absent."""
        import os
        try:
            os.remove("Base.json")
        except IOError:
            pass
        self.assertEqual(Base.load_from_file(), [])


if __name__ == "__main__":
    unittest.main()
