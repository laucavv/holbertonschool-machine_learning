#!/usr/bin/env python3
""" calculates sum{i=1}^n i^2 """


def summation_i_squared(n):
    """ calculates sum{i=1}^n i^2 """
    if type(n) is int:
        sum = (n * (n + 1) * (2 * n + 1)) // 6
        return (sum)
    else:
        return (None)
