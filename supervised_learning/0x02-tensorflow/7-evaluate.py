#!/usr/bin/env python3
"""481#7 - Evaluate"""

import tensorflow.compat.v1 as tf


def evaluate(X, Y, save_path):
    """evaluates the output of a neural network"""
    with tf.Session() as session:
        saver = tf.train.import_meta_graph(save_path + ".meta")
        saver.restore(session, save_path)

        x = tf.get_collection("x")[0]
        y = tf.get_collection("y")[0]
        y_pred = tf.get_collection("y_pred")[0]
        loss = tf.get_collection("loss")[0]
        accuracy = tf.get_collection("accuracy")[0]

        data_labels = {x: X, y: Y}
        network_prediction = session.run(y_pred, feed_dict=data_labels)
        network_accuracy = session.run(accuracy, feed_dict=data_labels)
        network_loss = session.run(loss, feed_dict=data_labels)

        return network_prediction, network_accuracy, network_loss
