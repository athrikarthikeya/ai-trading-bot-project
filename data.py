import yfinance as yf
import pandas as pd

def get_data(ticker="^NSEI"):
    df = yf.download(ticker, period="1y", interval="1d")

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    return df