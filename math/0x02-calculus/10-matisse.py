#!/usr/bin/env python3

""" calculates the derivative of a polynomial """


def poly_derivative(poly):
    """ calculates the derivative of a polynomial """

    if type(poly) is list and len(poly) > 0:

        if len(poly) == 1:
            return [0]

        derivative = [0 for a in range(len(poly) - 1)]

        for d in range(1, (len(derivative) + 1)):
            derivative[d - 1] = poly[d] * d

        return derivative
    else:
        return None
