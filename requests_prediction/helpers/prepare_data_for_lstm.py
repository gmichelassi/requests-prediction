import numpy as np
import pandas as pd

from sklearn.preprocessing import MinMaxScaler
from requests_prediction.helpers.split_data import split_data


scaler = MinMaxScaler(feature_range=(0, 1))


def prepare_data_for_lstm(data: pd.DataFrame, look_back: int = 1):
    amount_of_requests = data.to_numpy()

    normalized_data = scaler.fit_transform(amount_of_requests.reshape(-1, 1))

    x, y = [], []
    for i in range(len(normalized_data) - look_back - 1):
        x.append(normalized_data[i:(i + look_back), 0])
        y.append(normalized_data[i + look_back, 0])

    (training_features, training_labels), (validation_features, validation_labels), (testing_features, testing_labels)\
        = split_data(np.array(x), np.array(y))

    return (
        (reshape_data(training_features), training_labels),
        (reshape_data(validation_features), validation_labels),
        (reshape_data(testing_features), testing_labels)
    )


def reshape_data(data: np.ndarray):
    return np.reshape(data, (data.shape[0], 1, data.shape[1]))
