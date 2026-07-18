#!/usr/bin/python3
"""Defines a class Square with size and position attributes."""


class Square:
    """Represent a square, storing its size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): The (x, y) position of the square.
                Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
            TypeError: If position is not a tuple of 2 positive
                integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square, with validation.

        Args:
            value (int): The new size.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square, with validation.

        Args:
            value (tuple): The new (x, y) position.

        Raises:
            TypeError: If value is not a tuple of 2 positive
                integers.
        """
        if (type(value) is not tuple or len(value) != 2 or
                not all(type(n) is int for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the '#' character, offset by position.

        Prints nothing but an empty line if size is 0.
        """
        if self.__size == 0:
            print("")
            return
        print("\n" * self.__position[1], end="")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
