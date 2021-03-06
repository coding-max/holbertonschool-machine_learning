#!/usr/bin/env python3
"""529#3-5"""


class Exponential:
    """represents an exponential distribution"""

    def __init__(self, data=None, lambtha=1.):
        """sets the instance attribute lambtha"""
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = 1 / (sum(data) / len(data))

    def pdf(self, x):
        """calculates the value of the PDF for a given time period"""
        e = 2.7182818285
        λ = self.lambtha
        if x < 0:
            return 0
        return λ * (e ** (-λ * x))

    def cdf(self, x):
        """calculates the value of the CDF for a given time period"""
        e = 2.7182818285
        λ = self.lambtha
        if x < 0:
            return 0
        return 1 - e ** (-λ * x)
