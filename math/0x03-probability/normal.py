#!/usr/bin/env python3
"""529#6-9"""


class Normal:
    """represents a normal distribution"""

    def __init__(self, data=None, mean=0., stddev=1.):
        """sets the instance attributes mean and stddev"""
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.stddev = float(stddev)
            self.mean = float(mean)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = sum(data) / len(data)
            variance = sum((x - self.mean) ** 2 for x in data) / len(data)
            self.stddev = variance ** 0.5

    def z_score(self, x):
        """calculates the z-score of a given x-value"""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """calculates the x-value of a given z-score"""
        return z * self.stddev + self.mean

    def pdf(self, x):
        """calculates the value of the PDF for a given x-value"""
        π = 3.1415926536
        e = 2.7182818285
        μ = self.mean
        σ = self.stddev
        a = 1 / (σ * ((2 * π) ** (1 / 2)))
        b = (-1 / 2) * ((x - μ) / σ) ** 2
        return a * (e ** b)
