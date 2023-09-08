#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    its a function that divides all the elements of a matrix
    """
    if not all(isinstance(row, list) and all(isinstance(val, (int, float))
        for val in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of intagers/floats")
    if len(set(len(row) for row in matrix )) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result = []
    for row in matrix:
        new_row = [round(val / div, 2)for val in row]
        result.append(new_row)

    return result
