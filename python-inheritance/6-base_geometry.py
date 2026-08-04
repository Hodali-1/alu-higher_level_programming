#!/usr/bin/python3
"""Defines a class BaseGeometry with an unimplemented area method."""


class BaseGeometry:
    """Represent a base for geometric shapes."""

    def area(self):
        """Raise an exception; subclasses must implement this."""
        raise Exception("area() is not implemented")
