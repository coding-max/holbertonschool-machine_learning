#!/usr/bin/env python3
"""529#0"""


class Poisson:
    """represents a poisson distribution"""

    def __init__(self, data=None, lambtha=1.):
        """Sets the instance attribute lambtha"""
        e = 2.7182818285
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = sum(data) / len(data)
