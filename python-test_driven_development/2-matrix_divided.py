#!/usr/bin/python3
"""Provides a function that divides every element of a matrix.

This module demonstrates validating a nested list structure and
numeric input, then building a brand-new matrix rather than
mutating the one it was given.
"""


def matrix_divided(matrix, div):
    """Return a new matrix with every element divided by div.

    Args:
        matrix: A list of lists of integers or floats.
        div: The number to divide every element by.
    """
    if (type(matrix) is not list or len(matrix) == 0 or
            not all(type(row) is list for row in matrix) or
            not all(type(n) in (int, float)
                    for row in matrix for n in row)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(n / div, 2) for n in row] for row in matrix]
