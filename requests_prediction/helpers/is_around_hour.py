import pandas as pd


def is_around_hour(datetime: pd.Timestamp, hour: int) -> bool:
    return datetime.hour == hour and datetime.minute in [0, 5, 55]
