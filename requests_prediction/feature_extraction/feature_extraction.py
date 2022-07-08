import csv
import pandas as pd
import os

from requests_prediction.helpers import is_holiday, is_around_hour, is_super_peek, is_mini_peek


WEEKEND = ['saturday', 'sunday']
FILENAME = './requests_prediction/data/formatted_data.csv'
FIELDNAMES = [
    'day', 'month', 'hour', 'minute', 'holiday', 'super_peak', 'mini_peak', 'amount_of_requests'
]


def extract_features(data: pd.DataFrame) -> None:
    datetime_column = data['datetime']
    amount_column = data['amount']

    for datetime, amount_of_requests in zip(datetime_column, amount_column):
        day_name: str = datetime.day_name().lower()

        if day_name in WEEKEND:
            continue

        features = {
            'day': datetime.day,
            'month': datetime.month,
            'hour': datetime.hour,
            'minute': datetime.minute,
            'holiday': 1 if is_holiday(datetime) else 0,
            'super_peak': 1 if is_super_peek(datetime) else 0,
            'mini_peak': 1 if is_mini_peek(datetime) else 0,
            'amount_of_requests': amount_of_requests
        }

        with open(FILENAME, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
            should_write_header = os.stat(FILENAME).st_size == 0 if os.path.exists(FILENAME) else True
            writer.writeheader() if should_write_header else None
            writer.writerow(features)
