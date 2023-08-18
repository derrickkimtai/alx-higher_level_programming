#!/bin/usr/python3
def square_matrix_simple(matrix=[]):
    result = [[x ** 2 for x in row] for row in matrix]
    return result
