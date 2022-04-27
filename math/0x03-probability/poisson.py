#!/usr/bin/env python3
"""529#0"""


class Poisson:
    """represents a poisson distribution"""

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
            self.lambtha = sum(data) / len(data)

    def pmf(self, k):
        """calculates the value of the PMF for a given number of 'successes'"""
        k = int(k)
        e = 2.7182818285
        λ = self.lambtha

        return (e ** -λ) * (λ ** k) / self.factorial(k)

    def factorial(self, k):
        """calculates the factorial of k"""
        factorial = 1

        for n in range(1, k + 1):
            factorial = factorial * n
        return factorial
