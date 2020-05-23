import yfinance as yf

# Returns Pandas DataFrame with columns as
# Date, Open, High, Low, Close, Adj Close, Volume

# valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo; (optional, default is '1d')
# valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
# Date Format is "YYYY-MM-DD"
# fetch data by interval (including intraday if period < 60 days)


def _period(ticker, interval, period):  # Takes period as the input
    data = yf.download(tickers=ticker, interval=interval, period=period)
    return data


def _dates(ticker, interval, start_date, end_date):  # Takes dates range as the input
    data = yf.download(tickers=ticker, interval=interval, start=start_date, end=end_date)
    return data


if __name__ == '__main__':
    print(_period('AXISBANK.NS', '1d', '1d'))  # Testing on AXISBANK(NSE)


