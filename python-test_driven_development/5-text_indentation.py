#!/usr/bin/python3
"""Provides a function that prints text with extra line breaks.

This module demonstrates building output character by character,
inserting a blank line after each sentence-ending punctuation
mark while trimming stray whitespace from every printed segment.
"""


def text_indentation(text):
    """Print text, adding two newlines after '.', '?', or ':'.

    Args:
        text (str): The text to print.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    end_chars = ".?:"
    word = ""
    for char in text:
        if char == "\n":
            char = " "
        word += char
        if char in end_chars:
            print(word.strip())
            print()
            word = ""
    print(word.strip(), end="")
