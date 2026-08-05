#!/usr/bin/python3
"""Defines a function that deserializes a JSON string into an object."""
import json


def from_json_string(my_str):
    """Return an object represented by a JSON string.

    Args:
        my_str (str): A JSON-formatted string.

    Returns:
        The Python data structure represented by my_str.
    """
    return json.loads(my_str)
