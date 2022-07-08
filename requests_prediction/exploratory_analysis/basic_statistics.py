import pandas as pd


def basic_statistics(data: pd.DataFrame):
    print(f"Dataset shape: {data.shape}")
    print(f"Requets mean for all time: {data['amount'].mean():.2f}")
    print(f"Requests STD for all time: {data['amount'].std():.2f}")

    minimum_index = data['amount'].idxmin()
    maximum_index = data['amount'].idxmax()

    minimum = data.loc[minimum_index]
    maximum = data.loc[maximum_index]

    print(f"Min amount of requets was {minimum['amount']} and happened on {minimum['datetime']}")
    print(f"Max amount of requets was {maximum['amount']} and happened on {maximum['datetime']}")
