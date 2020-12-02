#!/usr/bin/env python3
""" adds two arrays element-wise """


def add_matrices2D(mat1, mat2):
    """  adds two arrays element-wise: """
    sum_matirx = []
    if len(mat1) == len(mat2) and len(mat1[0]) == len(mat2[0]):
        for i in range(len(mat1)):
            sum = []
            for j in range(len(mat2[0])):
                sum.append(mat1[i][j] + mat2[i][j])
            sum_matirx.append(sum)
        return sum_matirx
    else:
        return None
