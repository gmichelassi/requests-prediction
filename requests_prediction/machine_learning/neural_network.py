import numpy as np
import tensorflow as tf

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from requests_prediction.helpers import split_data
from requests_prediction.exploratory_analysis import plot_history, plot_predictions_comparison


def neural_network(features: np.ndarray, labels: np.ndarray):
    (training_features, training_labels), (validation_features, validation_labels), (testing_features, testing_labels) \
        = split_data(features, labels)

    model = Sequential([
        Dense(8, activation='relu', input_shape=[7]),
        Dense(8, activation='relu'),
        Dense(6, activation='relu'),
        Dense(1)
    ])
    optimizer = tf.keras.optimizers.RMSprop(0.01)

    model.compile(
        loss='mse',
        optimizer=optimizer,
        metrics=['mae', 'mse']
    )

    history = model.fit(
        training_features,
        training_labels,
        epochs=250,
        validation_data=(validation_features, validation_labels)
    )

    plot_history(history)

    predicted = model.predict(testing_features)

    plot_predictions_comparison(actual=testing_labels, predicted=predicted)
