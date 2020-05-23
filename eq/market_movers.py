import pandas as pd
import fetch_data, get_names


def _losers(start_date, end_date, interval):
    names = get_names._string()
    data = fetch_data._dates(names, interval, start_date, end_date)
    close_start_date = data['Close'][:1]
    close_end_date = data['Close'][-1:]
    close_difference = (close_end_date.reset_index(drop=True) - close_start_date.reset_index(drop=True))
    close_difference_percent = close_difference / close_start_date.reset_index(drop=True) * 100
    close_difference_percent = close_difference_percent.sort_values(by=0, axis=1)
    return close_difference_percent


def _gainers(start_date, end_date, interval):
    close_difference_percent = _losers(start_date, end_date, interval)
    return close_difference_percent.sort_values(by=0, axis=1, ascending=False)


if __name__ == "__main__":
    print(_gainers('2020-05-04', '2020-05-23', '1d').transpose())
