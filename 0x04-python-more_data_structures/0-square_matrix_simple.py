#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_squared = []
    for i in matrix:  # each line
        matrix_squared.append([j**2 for j in i])  # j is for each item in i
    return (matrix_squared)
