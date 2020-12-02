#!/usr/bin/env python3

"""  Calculates the shape of a matrix """


def matrix_shape(matrix):
    """ shape of matrix """
    shape_matrix = []
    if type(matrix) is list:
        shape_matrix.append(len(matrix))
        shape_matrix += matrix_shape(matrix[0])

    return shape_matrix
