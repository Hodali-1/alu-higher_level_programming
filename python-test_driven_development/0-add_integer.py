#!/usr/bin/python3
"""Provides a function that adds two numbers as integers.

This module demonstrates basic type validation and casting
floats to integers before performing addition, a small example
of test-driven development using interactive doctests.
"""


def add_integer(a, b=98):
    """Add two numbers, casting floats to integers first.

    Args:
        a: The first number (int or float).
        b: The second number (int or float). Defaults to 98.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
