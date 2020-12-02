#!/usr/bin/env python3
""" adds two arrays element-wise """


def add_arrays(arr1, arr2):
    """  adds two arrays element-wise: """
    if len(arr1) == len(arr2):
        sum = list(map(lambda a, b: a + b, arr1, arr2))
        return sum

    return None
