#!/usr/bin/env python3
"""  the transpose of a 2D matrix """


def matrix_transpose(matrix):
    """ returns the transpose of a 2D matrix """
    transpose = []
    for i in range(len(matrix[0])):
        inver = []
        for j in range(len(matrix)):
            inver.append(matrix[j][i])
        transpose.append(inver)
    return transpose
