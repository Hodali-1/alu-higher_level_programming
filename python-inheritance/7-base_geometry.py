#!/usr/bin/python3
"""Defines a class BaseGeometry with area and integer validation."""


class BaseGeometry:
    """Represent a base for geometric shapes."""

    def area(self):
        """Raise an exception; subclasses must implement this."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer.

        Args:
            name (str): The name of the value, used in error messages.
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
