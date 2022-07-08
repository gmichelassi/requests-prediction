import pandas as pd


SUPER_PEAK_HOURS = [7, 8, 12, 13, 14, 17, 18]


def is_super_peek(datetime: pd.Timestamp):
    return datetime.hour in SUPER_PEAK_HOURS and datetime.minute == 0
