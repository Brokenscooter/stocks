import fetch_data, get_names
from datetime import date
import datetime
import numpy as np


def _spread(tickers, period, start_date, end_date):
    data = fetch_data._dates(tickers, period, start_date, end_date)
    spread_percent = ((data['High'] - data['Low']) / data['High'] * 100).round(1)
    mean = np.mean(spread_percent.transpose(), axis=1)
    mean = mean.to_frame()  # Converting Core.Series to DataFrame
    mean.columns = ['Average']  # Naming the column
    return np.round(mean.sort_values("Average"), 2)


if __name__ == '__main__':
    tomorrow = date.today() + datetime.timedelta(days=1)
    today_5 = date.today() + datetime.timedelta(days=-15)

    ticker = get_names._string()
    print(_spread(ticker, '1d', today_5, tomorrow))
