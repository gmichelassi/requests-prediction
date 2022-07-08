import pandas as pd

from datetime import datetime
from requests_prediction.exploratory_analysis import basic_statistics, range_visualization
from requests_prediction.machine_learning import neural_network, lstm


def run_analysis(data: pd.DataFrame):
    basic_statistics(data)

    range_visualization(
        data=data,
        start_date=datetime.fromisoformat('2022-04-24T00:00:00'),
        end_date=datetime.fromisoformat('2022-04-30T00:00:00')
    )


def main(show_analysis: bool, use_nn: bool, use_lstm: bool):
    if show_analysis:
        data = pd.read_csv(
            filepath_or_buffer='./requests_prediction/data/requests.csv',
            parse_dates=["datetime"]
        )

        run_analysis(data)

    dataset = pd.read_csv(
        filepath_or_buffer='./requests_prediction/data/formatted_data.csv'
    )

    if use_nn:
        features = dataset.iloc[:, :-1].to_numpy()
        labels = dataset.iloc[:, -1].to_numpy()
        neural_network(features=features, labels=labels)

    if use_lstm:
        lstm(data=dataset.iloc[:, -1], look_back=3)
