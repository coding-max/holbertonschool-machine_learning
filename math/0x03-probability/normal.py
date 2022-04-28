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
            self.stddev = 0
            for i in range(len(data) - 1):
                self.stddev += ((data[i] - self.mean) ** 2) / len(data)
            self.stddev = self.stddev ** 0.5

    def z_score(self, x):
        """calculates the z-score of a given x-value"""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """calculates the x-value of a given z-score"""
        return z * self.stddev + self.mean
