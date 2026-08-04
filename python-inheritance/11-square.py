#!/usr/bin/python3
"""Defines a class Square with its own string representation."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square as a special case of Rectangle."""

    def __init__(self, size):
        """Initialize a new Square instance.

        Args:
            size (int): The size of each side of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is not greater than 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return the string representation of the square."""
        w = self._Rectangle__width
        h = self._Rectangle__height
        return "[Square] {}/{}".format(w, h)
