#!/usr/bin/python3
"""Unit tests for the Square class."""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Cover construction, validation, update and I/O of Square."""

    def test_valid(self):
        """Valid constructions set every attribute correctly."""
        self.assertEqual(Square(1).size, 1)
        self.assertEqual(Square(1, 2).x, 2)
        self.assertEqual(Square(1, 2, 3).y, 3)
        self.assertEqual(Square(1, 2, 3, 4).id, 4)
        self.assertEqual(str(Square(5, 2, 1, 3)), "[Square] (3) 2/1 - 5")
        self.assertEqual(Square(3, 1, 2, 9).to_dictionary(),
                         {"id": 9, "size": 3, "x": 1, "y": 2})

    def test_type_errors(self):
        """Non-integer size, x, y each raise TypeError."""
        cases = [(("1",), "width must be an integer"),
                 ((1, "2"), "x must be an integer"),
                 ((1, 2, "3"), "y must be an integer")]
        for args, msg in cases:
            with self.assertRaises(TypeError) as e:
                Square(*args)
            self.assertEqual(str(e.exception), msg)

    def test_value_errors(self):
        """Out-of-range size, x, y each raise ValueError."""
        cases = [((-1,), "width must be > 0"),
                 ((0,), "width must be > 0"),
                 ((1, -2), "x must be >= 0"),
                 ((1, 2, -3), "y must be >= 0")]
        for args, msg in cases:
            with self.assertRaises(ValueError) as e:
                Square(*args)
            self.assertEqual(str(e.exception), msg)

    def test_size_setter(self):
        """Setting size updates both width and height."""
        s = Square(1)
        s.size = 7
        self.assertEqual((s.width, s.height), (7, 7))

    def test_update(self):
        """update() works with positional args and with kwargs."""
        s = Square(1)
        s.update(89, 1, 2, 3)
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")
        s.update(**{"id": 7, "size": 4, "x": 5, "y": 6})
        self.assertEqual(str(s), "[Square] (7) 5/6 - 4")

    def test_create_and_files(self):
        """create(), save_to_file() and load_from_file() round-trip."""
        import os
        s = Square.create(**{"id": 89, "size": 1, "x": 2, "y": 3})
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")
        Square.save_to_file(None)
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")
        Square.save_to_file([])
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")
        Square.save_to_file([Square(1)])
        with open("Square.json") as f:
            self.assertIn('"size": 1', f.read())
        os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])
        Square.save_to_file([Square(2, 3, 4, 5)])
        self.assertEqual(str(Square.load_from_file()[0]),
                         "[Square] (5) 3/4 - 2")


if __name__ == "__main__":
    unittest.main()
