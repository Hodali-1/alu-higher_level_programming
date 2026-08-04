#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle."""
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
