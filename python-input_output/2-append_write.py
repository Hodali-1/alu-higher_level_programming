#!/usr/bin/python3
"""Defines a function that appends a string to the end of a text file."""


def append_write(filename="", text=""):
    """Append text to the end of a UTF8 file, creating it if needed.

    Args:
        filename (str): The path of the file to append to.
        text (str): The text to append.

    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
