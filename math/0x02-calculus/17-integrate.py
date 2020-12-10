#!/usr/bin/env python3

""" calculates the integral of a polynomial """


def poly_integral(poly, C=0):
    """ calculates the integral of a polynomial """

    if type(poly) is list and len(poly) > 0 and isinstance(C, (int, float)):

        derivative = [0 for a in range(len(poly) + 1)]
        derivative[0] = C

        for d in range(1, (len(derivative))):
            if poly[d - 1] % d == 0:
                derivative[d] = poly[d - 1] // d
            else:
                derivative[d] = poly[d - 1] / d

        return derivative
    else:
        return None
