#!/usr/bin/python3
"""Defines a function that returns a dict representation of an object."""


def class_to_json(obj):
    """Return the dictionary description of a simple-attribute object.

    Args:
        obj: An instance of a class with only JSON-serializable
            attributes (list, dict, str, int, bool).

    Returns:
        dict: obj's instance attributes as a dictionary.
    """
    return obj.__dict__
