#!/usr/bin/env python3
""" slices a matrix along specific axes """


def np_slice(matrix, axes={}):
    """ slices a matrix along specific axes """
    mat_new = [slice(None)] * len(matrix.shape)
    for key, value in axes.items():
        mat_new[key] = slice(*value)
    return marix[tuple(mat_new)]
