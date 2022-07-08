import pandas as pd


BUSINESS_HOURS = list(range(6, 20))


def is_mini_peek(datetime: pd.Timestamp):
    return datetime.hour in BUSINESS_HOURS and datetime.minute == 30
