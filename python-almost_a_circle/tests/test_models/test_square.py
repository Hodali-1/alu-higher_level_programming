#!/usr/bin/python3
"""Unit tests for the Square class."""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for size handling and serialization of Square."""

    def test_str(self):
        """__str__ follows the required format."""
        self.assertEqual(str(Square(5, 2, 1, 3)), "[Square] (3) 2/1 - 5")

    def test_size_getter(self):
        """size returns the width."""
        self.assertEqual(Square(7).size, 7)

    def test_size_setter_validation(self):
        """Setting an invalid size raises TypeError."""
        s = Square(1)
        with self.assertRaises(TypeError) as e:
            s.size = "x"
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_update_args(self):
        """update() assigns positional args in id, size, x, y order."""
        s = Square(1)
        s.update(89, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (89) 3/4 - 2")

    def test_to_dictionary(self):
        """to_dictionary() returns id, size, x and y."""
        self.assertEqual(
            Square(3, 1, 2, 9).to_dictionary(),
            {"id": 9, "size": 3, "x": 1, "y": 2})


if __name__ == "__main__":
    unittest.main()
