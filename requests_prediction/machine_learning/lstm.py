import pandas as pd

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, LSTM
from requests_prediction.helpers import prepare_data_for_lstm
from requests_prediction.exploratory_analysis import plot_history, plot_predictions_comparison


def lstm(data: pd.DataFrame, look_back: int = 5):
    (training_features, training_labels), (validation_features, validation_labels), (testing_features, testing_labels)\
        = prepare_data_for_lstm(data, look_back)

    print(training_features)

    model = Sequential([
        LSTM(10, input_shape=(1, look_back)),
        Dense(1)
    ])

    model.compile(
        loss='mse',
        optimizer='adam',
        metrics=['mae', 'mse']
    )

    history = model.fit(
        training_features,
        training_labels,
        epochs=10,
        validation_data=(validation_features, validation_labels)
    )

    plot_history(history)

    predicted = model.predict(testing_features)

    plot_predictions_comparison(actual=testing_labels, predicted=predicted.flatten())
