#!/usr/bin/env python3
"""529#10-12"""


class Binomial:
    """represents a binomial distribution"""

    def __init__(self, data=None, n=1, p=0.5):
        """sets the instance attributes n and p"""
        self.n = n
        self.p = p

        if n < 1:
            raise ValueError("n must be a positive value")
        if p <= 0 or p >= 1:
            raise ValueError("p must be greater than 0 and less than 1")
        if data is not None:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
