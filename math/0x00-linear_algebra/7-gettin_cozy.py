#!/usr/bin/env python3
"""  concatenates two arrays """


def cat_matrices2D(mat1, mat2, axis=0):
    """  concatenates two arrays """

    arr = []
    copy_mat1 = [row[:] for row in mat1]
    copy_mat2 = [row[:] for row in mat2]

    if axis == 0 and len(mat1[0]) == len(mat2[0]):
        copy_mat1.extend(mat2)
        return copy_mat1
    elif axis == 1 and len(mat1) == len(mat2):
        for i in range(len(mat1)):
            arr.append(copy_mat1[i] + copy_mat2[i])
        return arr
    else:
        return None
