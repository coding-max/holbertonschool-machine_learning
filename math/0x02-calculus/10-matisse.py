#!/usr/bin/env python3
"""471#10"""


def poly_derivative(poly):
    """calculates the derivative of a polynomial"""
    if (not isinstance(poly, list) or any
       (not isinstance(x, (int, float)) for x in poly)):
        return None
    derivative = [poly[i] * i for i in range(1, len(poly))]
    return [0] if len(derivative) == 0 else derivative
