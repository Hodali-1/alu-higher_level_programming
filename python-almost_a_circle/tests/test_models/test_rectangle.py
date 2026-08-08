#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for validation, geometry and serialization of Rectangle."""

    def test_area(self):
        """area() returns width times height."""
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_str(self):
        """__str__ follows the required format."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_width_type(self):
        """A non-integer width raises TypeError."""
        with self.assertRaises(TypeError) as e:
            Rectangle("4", 2)
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_width_value(self):
        """A non-positive width raises ValueError."""
        with self.assertRaises(ValueError) as e:
            Rectangle(0, 2)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_x_value(self):
        """A negative x raises ValueError."""
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 1, -1)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def test_update_args(self):
        """update() assigns positional args in id, w, h, x, y order."""
        r = Rectangle(1, 1)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """update() assigns keyword args when no positionals are given."""
        r = Rectangle(1, 1)
        r.update(width=2, x=3)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.x, 3)

    def test_to_dictionary(self):
        """to_dictionary() returns all attributes."""
        r = Rectangle(10, 2, 1, 9, 1)
        self.assertEqual(
            r.to_dictionary(),
            {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9})


if __name__ == "__main__":
    unittest.main()
