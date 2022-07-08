import numpy as np


def split_data(features: np.ndarray, labels: np.ndarray):
    size = len(features)

    training_features = features[0:int(size * 0.7)]
    training_labels = labels[0:int(size * 0.7)]

    validation_features = features[int(size * 0.7):int(size * 0.9)]
    validation_labels = labels[int(size * 0.7):int(size * 0.9)]

    testing_features = features[int(size * 0.9):]
    testing_labels = labels[int(size * 0.9):]

    return (
        (training_features, training_labels),
        (validation_features, validation_labels),
        (testing_features, testing_labels)
    )
