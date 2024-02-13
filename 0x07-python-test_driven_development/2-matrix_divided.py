#!/usr/bin/python3
"""Divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """
    Args:
    matrix (list of lists): The input matrix.
    div (int or float): The divisor.

    Returns:
    list of lists: A new matrix.

    Raises:
    TypeError: If matrix is not a list of lists.
    ZeroDivisionError: If div is equal to 0.
    """
    err = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        if not all(isinstance(row, list) for row in matrix):
            raise TypeError(f"{err}")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    r_matrix = []
    for row in matrix:
        n_row = [round(n / div, 2) for n in row]
        r_matrix.append(n_row)
    return r_matrix
