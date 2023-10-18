import pandas as pd 
import pandas_datareader as pdr

API_KEY = '3KCUP943508G9N7E'

stocks = ['AMZN', 'AAPL', 'META', 'NVDA', 'TSLA', 'MSFT', 'GOOG', 'BRK.B', 'SPY']
def extractData(tickers: str):
    all_data = pd.DataFrame()

    for ticker in tickers:
        ts = pdr.av.time_series.AVTimeSeriesReader(tickers, api_key=API_KEY)
        df = ts.read()
        df.index = pd.to_datetime(df.index, format='%Y-%m-%d')
        df['Ticker'] = ticker
        all_data = all_data.append(df)

    all_data.to_csv('../data/histData.csv')

if __name__ == '__main__':
    extractData(stocks)

import yfinance as yf
from datetime import datetime

tsla = yf.Ticker('TSLA')

end_date = datetime.now().strftime('%Y-%m-%d')
hist_data = tsla.history(start='2022-01-01', end = end_date)

hist_data.drop(columns=['Dividends', 'Stock Splits'], inplace=True)

hist_data.to_csv('./data/tsla_daily.csv')
