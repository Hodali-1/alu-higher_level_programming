#!/usr/bin/python3
"""Defines a class Square with a private size attribute."""


class Square:
    """Represent a square, storing its size as a private attribute."""

    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square. Defaults to 0.
        """
        self.__size = size
