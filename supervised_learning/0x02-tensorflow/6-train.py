#!/usr/bin/env python3
"""481#6 - Train"""

import tensorflow.compat.v1 as tf
calculate_accuracy = __import__('3-calculate_accuracy').calculate_accuracy
calculate_loss = __import__('4-calculate_loss').calculate_loss
create_placeholders = __import__('0-create_placeholders').create_placeholders
create_train_op = __import__('5-create_train_op').create_train_op
forward_prop = __import__('2-forward_prop').forward_prop


def train(X_train, Y_train, X_valid, Y_valid, layer_sizes, activations,
          alpha, iterations, save_path="/tmp/model.ckpt"):
    """builds, trains, and saves a neural network classifier"""
    x, y = create_placeholders(X_train.shape[1], Y_train.shape[1])
    tf.add_to_collection("x", x)
    tf.add_to_collection("y", y)

    y_pred = forward_prop(x, layer_sizes, activations)
    tf.add_to_collection("y_pred", y_pred)

    loss = calculate_loss(y, y_pred)
    tf.add_to_collection("loss", loss)

    accuracy = calculate_accuracy(y, y_pred)
    tf.add_to_collection("accuracy", accuracy)

    training = create_train_op(loss, alpha)
    tf.add_to_collection("train", train)

    init = tf.global_variables_initializer()
    saver = tf.train.Saver()

    with tf.Session() as session:
        session.run(init)
        for i in range(iterations + 1):
            t_data = {x: X_train, y: Y_train}
            training_cost = session.run(loss, feed_dict=t_data)
            training_accuracy = session.run(accuracy, feed_dict=t_data)
            v_data = {x: X_valid, y: Y_valid}
            validation_cost = session.run(loss, feed_dict=v_data)
            validation_accuracy = session.run(accuracy, feed_dict=v_data)
            if i % 100 == 0 or i == iterations:
                print("After {} iterations:".format(i))
                print("\tTraining Cost: {}".format(training_cost))
                print("\tTraining Accuracy: {}".format(training_accuracy))
                print("\tValidation Cost: {}".format(validation_cost))
                print("\tValidation Accuracy: {}".format(validation_accuracy))
            if i < iterations:
                session.run(training, feed_dict=t_data)
        return saver.save(session, save_path)
