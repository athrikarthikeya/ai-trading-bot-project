import ta

def add_indicators(df):
    close = df['Close'].squeeze()

    df['RSI'] = ta.momentum.RSIIndicator(close).rsi()
    df['MACD'] = ta.trend.MACD(close).macd()

    df['SMA'] = ta.trend.SMAIndicator(close, window=14).sma_indicator()
    df['EMA'] = ta.trend.EMAIndicator(close, window=14).ema_indicator()

    df['Volatility'] = close.pct_change().rolling(10).std()

    df['Momentum'] = close - close.shift(5)

    return df