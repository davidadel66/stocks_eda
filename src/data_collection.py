import pandas as pd 
import yfinance as yf
from datetime import datetime

if __name__ == '__main__':
    tickers = ['TSLA', 'AMZN', 'AAPL', 'NVDA', 'MSFT', 'META', 'SPY']
    for stock in tickers:
        ticker = yf.Ticker(stock)
        end_date = datetime.now().strftime('%Y-%m-%d')
        hist_data = ticker.history(start='2020-01-01', end = end_date)

        hist_data.drop(columns=['Dividends', 'Stock Splits'], inplace=True)

        hist_data.to_csv(f'./data/{stock}_daily.csv')
