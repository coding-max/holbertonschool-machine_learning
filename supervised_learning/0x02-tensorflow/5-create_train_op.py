#!/usr/bin/env python3
"""481#5 - Train_Op"""

import tensorflow.compat.v1 as tf


def create_train_op(loss, alpha):
    """creates the training operation for the network"""
    return tf.train.GradientDescentOptimizer(alpha).minimize(loss)
