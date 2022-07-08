import matplotlib.pyplot as plt
import numpy as np


def plot_predictions_comparison(actual: np.ndarray, predicted: np.ndarray):
    plt.figure()
    plt.xlabel('Time')
    plt.ylabel('Amount of Requests')
    plt.plot(list(range(len(actual))), actual, label='Actual Amount')
    plt.plot(list(range(len(predicted))), predicted, label='Predicted Amount')
    plt.legend()

    plt.show()
