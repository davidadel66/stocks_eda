import pandas as pd 
import yfinance as yf
from datetime import datetime

if __name__ == '__main__':
    tsla = yf.Ticker('TSLA')

    end_date = datetime.now().strftime('%Y-%m-%d')
    hist_data = tsla.history(start='2020-01-01', end = end_date)

    hist_data.drop(columns=['Dividends', 'Stock Splits'], inplace=True)

    hist_data.to_csv('./data/tsla_daily.csv')
