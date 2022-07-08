import pandas as pd

from datetime import datetime
from .visualization import visualization


def range_visualization(data: pd.DataFrame, start_date: datetime, end_date: datetime) -> None:
    mask = (data['datetime'] > start_date) & (data['datetime'] <= end_date)

    visualization(data=data.loc[mask])
