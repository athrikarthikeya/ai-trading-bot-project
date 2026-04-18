import mplfinance as mpf
import numpy as np

def plot_chart(df):
    buy_signals = np.where(df['Buy'], df['Low'] * 0.98, np.nan)
    sell_signals = np.where(df['Sell'], df['High'] * 1.02, np.nan)

    apds = [
        mpf.make_addplot(df['RSI'], panel=1, ylabel='RSI'),
    ]

    if np.any(df['Buy']):
        apds.append(
            mpf.make_addplot(buy_signals, type='scatter', marker='^', markersize=100)
        )

    if np.any(df['Sell']):
        apds.append(
            mpf.make_addplot(sell_signals, type='scatter', marker='v', markersize=100)
        )

    mpf.plot(
        df,
        type='candle',
        style='charles',
        addplot=apds,
        volume=True,
        title="AI Trading Bot",
        figsize=(12, 8)
    )