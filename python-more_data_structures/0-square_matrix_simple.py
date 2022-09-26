#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []

    for lst in matrix:
        new_matrix.append(list(map(lambda x: x ** 2, lst)))

    return new_matrix
