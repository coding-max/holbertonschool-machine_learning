#!/usr/bin/env python3
"""481#0 - Placeholders"""

import tensorflow.compat.v1 as tf


def create_placeholders(nx, classes):
    """returns two placeholders, x and y, for the neural network"""
    x = tf.placeholder(float, (None, nx), "x")
    y = tf.placeholder(float, (None, classes), "y")
    return x, y
