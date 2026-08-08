#!/usr/bin/python3
"""Provides a function that prints a square made of '#' characters.

This module demonstrates that checking an argument's exact type
before checking its value naturally handles a tricky edge case:
a negative float must be reported as a type error, not a value
error, simply because the type check runs first.
"""


def print_square(size):
    """Print a square of '#' characters, size x size.

    Args:
        size (int): The length of each side of the square.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
