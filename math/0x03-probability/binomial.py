#!/usr/bin/env python3
"""  class Binomial that represents a binomial distribution """


class Binomial:
    """  class Binomial that represents a binomial distribution """
    def __init__(self, data=None, n=1, p=0.5):
        """ class contructor """
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            else:
                self.n = int(n)
                self.p = float(p)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                mean = float(sum(data)/len(data))
                variance = float(sum((x - mean)**2 for x in data) /
                                 len(data))
                p = 1 - variance/mean
                self.n = round(mean/p)
                self.p = float(mean/self.n)

    def pmf(self, k):
        """ Calculates the value of the PMF for a
            given number of “successes”
        """
        if type(k) is not int:
            k = int(k)
        if k < 0 or k > self.n:
            return 0

        return (self.factorial(self.n)*self.p**k*(1-self.p)**(self.n - k) /
                (self.factorial(self.n - k)*self.factorial(k)))

    def factorial(self, k):
        """ auxiliary function to calculate the factorial
        of a number
        """
        if k == 0:
            return 1
        else:
            return (k * self.factorial(k-1))

    def cdf(self, k):
        """ Calculates the value of the CDF for
            a given number of “successes”
        """
        k = int(k)
        if k < 0 or k > self.n:
            return 0
        cdf = 0
        for i in range(0, k+1):
            cdf += self.pmf(i)
        return cdf
