#!/usr/bin/python3
"""
Divides all elements of a matrix by a given number.
"""


def matrix_divided(matrix, div):
    """
    Args:
        matrix (list): A list of lists containing integers or floats.
        div (int or float): The number to divide the matrix elements by.

    Returns:
        list: A new matrix with elements divided by div, rounded to 2 dec.

    Raises:
        TypeError: If the matrix is not a matrix of integers/floats,
        or if each row doesn't have the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to zero.
    """

    if not all(isinstance(row, list) and
               all(isinstance(elem, (int, float)) for elem in row)
               for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return new_matrix
