#!/usr/bin/env python3
"""  class Exponential that represents an exponential distribution """


class Exponential():
    """  class exponencial """
    def __init__(self, data=None, lambtha=1):
        """ class contructor """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            else:
                self.lambtha = float(lambtha)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            self.lambtha = float(1 / (sum(data)/len(data)))

    def factorial(self, k):
        """ auxiliary function to calculate the factorial
         of a number """

        if k == 0:
            return 1
        return(k * self.factorial(k - 1))

    def pdf(self, x):
        """ Calculates the value of the PDF for
        a given time period
        """

        if x < 0:
            return 0
        else:
            e = 2.7182818285
            return (((self.lambtha)*(e**(self.lambtha*(-1) * x))))

    def cdf(self, x):
        """ Calculates the value of the CDF for a
        given time period """

        if x < 0:
            return 0
        else:
            cdf = 0
            e = 2.7182818285
            cdf = (1-(e**(self.lambtha*(-1) * x)))
        return cdf
