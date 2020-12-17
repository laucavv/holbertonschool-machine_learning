#!/usr/bin/env python3
""" class Normal that represents a normal distribution """


class Normal():
    """ class Normal that represents a normal distribution """
    def __init__(self, data=None, mean=0., stddev=1.):
        """ class contructor """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            else:
                self.mean = float(mean)
                self.stddev = float(stddev)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            self.mean = float(sum(data)/len(data))
            self.stddev = float(sum((x - self.mean)**2 for x in data) /
                                len(data))**0.5

    def z_score(self, x):
        """ Calculates the z-score of a given x-value """
        value = 0
        value = ((x - self.mean) / self.stddev)
        return value

    def x_value(self, z):
        """ Calculates the x-value of a given z-score  """
        value = 0
        value = ((z*self.stddev) + self.mean)
        return value

    def pdf(self, x):
        """ Calculates the value of the PDF for a given x-value  """
        value = 0
        e = 2.7182818285
        pi = 3.1415926536
        value = (e**((-1*(x - self.mean)**2)/(2*self.stddev**2)) /
                 (self.stddev*(2*pi)**0.5))
        return value

    def fun_error(self, x):
        """ aux error calcualte """
        error = 0
        pi = 3.1415926536
        error = ((2/(pi**0.5)) *
                 (x - (x**3) / 3 + (x**5) / 10 - (x**7) / 42 + (x**9) / 216))
        return error

    def cdf(self, x):
        """ Calculates the value of the CDF for a given x-value """
        value = 0
        value = (0.5 * (1 + self.fun_error((x-self.mean)
                 / (self.stddev*(2**0.5)))))
        return value
