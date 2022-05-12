#!/usr/bin/env python3
"""481#2 - Forward Propagation"""

import tensorflow.compat.v1 as tf
create_layer = __import__('1-create_layer').create_layer


def forward_prop(x, layer_sizes=[], activations=[]):
    """creates the forward propagation graph for the neural network"""
    prediction = create_layer(x, layer_sizes[0], activations[0])
    for i in range(1, len(layer_sizes)):
        prediction = create_layer(prediction, layer_sizes[i], activations[i])
    return prediction
