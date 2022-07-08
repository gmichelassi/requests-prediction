import pandas as pd

from datetime import date


HOLIDAYS = {
    'new-years-day': date(year=2022, month=1, day=1),
    'carnival': date(year=2022, month=3, day=1),
    'good-friday': date(year=2022, month=4, day=15),
    'easter': date(year=2022, month=4, day=17),
    'tiradentes': date(year=2022, month=4, day=21),
    'labors-day': date(year=2022, month=5, day=1),
    'corpus-christi': date(year=2022, month=6, day=16),
    'independence-day': date(year=2022, month=9, day=7),
    'nossa-senhora-aparecida': date(year=2022, month=10, day=12),
    'all-souls-day': date(year=2022, month=11, day=2),
    'proclamation-of-republic': date(year=2022, month=11, day=15),
    'christmas': date(year=2022, month=12, day=25),
}


def is_holiday(datetime: pd.Timestamp) -> bool:
    return datetime.date() in list(HOLIDAYS.values())
