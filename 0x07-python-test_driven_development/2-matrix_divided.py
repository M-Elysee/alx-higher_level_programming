#!/usr/bin/python3
""" ***Divide a matrix*** """


def r(num, n):
    """ round a num to the nearest n th decimal place """
    return int(num * (10 ** n) + 0.5) / (10 ** n)


def matrix_divided(matrix, div):
    """ this function divide all elements of a matrix by div """
    if (not matrix or any(any(type(col) not in [int, float] for col in row)
       for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[r(col / div, 2) for col in row] for row in matrix]
