#!/usr/bin/env python3
"""471#9"""


def summation_i_squared(n):
    """calculates sum_{i=1}^{n} i^2"""
    if not isinstance(n, int):
        return None
    return sum(map(lambda i: i ** 2, range(1, n + 1)))
