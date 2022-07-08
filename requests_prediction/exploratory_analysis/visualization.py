import matplotlib.pyplot as plt
import pandas as pd


def visualization(data: pd.DataFrame) -> None:
    datetime = data['datetime']
    amount = data['amount']

    plt.figure(figsize=(20, 10))
    plt.plot(datetime, amount)
    plt.xlabel('Date Time')
    plt.ylabel('Amount of Requests')
    plt.title('Requests Overtime')

    plt.xticks(rotation=45)

    plt.show()
