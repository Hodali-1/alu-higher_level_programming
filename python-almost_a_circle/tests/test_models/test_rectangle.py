#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import unittest
import io
from contextlib import redirect_stdout
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Cover construction, validation, geometry and I/O of Rectangle."""

    def test_valid(self):
        """Valid constructions set every attribute correctly."""
        self.assertEqual(Rectangle(1, 2).width, 1)
        self.assertEqual(Rectangle(1, 2).height, 2)
        self.assertEqual(Rectangle(1, 2, 3).x, 3)
        self.assertEqual(Rectangle(1, 2, 3, 4).y, 4)
        self.assertEqual(Rectangle(1, 2, 3, 4, 5).id, 5)
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(str(Rectangle(4, 6, 2, 1, 12)),
                         "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(Rectangle(10, 2, 1, 9, 1).to_dictionary(),
                         {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9})

    def test_type_errors(self):
        """Non-integer width, height, x, y each raise TypeError."""
        cases = [(("1", 2), "width must be an integer"),
                 ((1, "2"), "height must be an integer"),
                 ((1, 2, "3"), "x must be an integer"),
                 ((1, 2, 3, "4"), "y must be an integer")]
        for args, msg in cases:
            with self.assertRaises(TypeError) as e:
                Rectangle(*args)
            self.assertEqual(str(e.exception), msg)

    def test_value_errors(self):
        """Out-of-range width, height, x, y each raise ValueError."""
        cases = [((-1, 2), "width must be > 0"),
                 ((0, 2), "width must be > 0"),
                 ((1, -2), "height must be > 0"),
                 ((1, 0), "height must be > 0"),
                 ((1, 2, -3), "x must be >= 0"),
                 ((1, 2, 3, -4), "y must be >= 0")]
        for args, msg in cases:
            with self.assertRaises(ValueError) as e:
                Rectangle(*args)
            self.assertEqual(str(e.exception), msg)

    def test_display(self):
        """display() honors x and y in all combinations."""
        cases = [(Rectangle(2, 2), "##\n##\n"),
                 (Rectangle(2, 2, 2), "  ##\n  ##\n"),
                 (Rectangle(2, 2, 2, 1), "\n  ##\n  ##\n")]
        for rect, out in cases:
            f = io.StringIO()
            with redirect_stdout(f):
                rect.display()
            self.assertEqual(f.getvalue(), out)

    def test_update(self):
        """update() works with positional args and with kwargs."""
        r = Rectangle(1, 1)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")
        r.update(**{"id": 7, "width": 5, "height": 6, "x": 8, "y": 9})
        self.assertEqual(str(r), "[Rectangle] (7) 8/9 - 5/6")

    def test_create_and_files(self):
        """create(), save_to_file() and load_from_file() round-trip."""
        import os
        r = Rectangle.create(**{"id": 89, "width": 1, "height": 2,
                                "x": 3, "y": 4})
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")
        Rectangle.save_to_file([])
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")
        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json") as f:
            self.assertIn('"width": 1', f.read())
        os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])
        Rectangle.save_to_file([Rectangle(1, 2, 3, 4, 5)])
        self.assertEqual(str(Rectangle.load_from_file()[0]),
                         "[Rectangle] (5) 3/4 - 1/2")


if __name__ == "__main__":
    unittest.main()
