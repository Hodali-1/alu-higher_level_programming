#!/usr/bin/python3
"""Defines a function that creates an object from a JSON file."""
import json


def load_from_json_file(filename):
    """Read a JSON file and return the object it represents.

    Args:
        filename (str): The path of the file to read.

    Returns:
        The Python data structure stored in the file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
