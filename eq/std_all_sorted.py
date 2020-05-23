import fetch_data, get_names


def low_high(start_date, end_date, interval):
    names = get_names._string()
    data = fetch_data._dates(names, interval, start_date, end_date)
    return data['Low'].std().sort_values(), data['High'].std().sort_values()
    # return data['Close'].std().sort_values()


if __name__ == '__main__':
    print(low_high('2019-12-01', '2019-12-31', '1d'))