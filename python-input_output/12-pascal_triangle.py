#!/usr/bin/python3
"""Defines a function that builds Pascal's Triangle."""


def pascal_triangle(n):
    """Return Pascal's Triangle of n rows as a list of lists.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of n rows, or an empty list if n <= 0.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        row = [1]
        for j in range(len(prev_row) - 1):
            row.append(prev_row[j] + prev_row[j + 1])
        row.append(1)
        triangle.append(row)
    return triangle
