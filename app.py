import streamlit as st
from data import get_data
from indicators import add_indicators
from model import create_target, train_model, generate_signals
from backtest import backtest
import mplfinance as mpf
import numpy as np

st.title("📈 AI Trading Bot Dashboard")

ticker = st.text_input("Enter Stock Ticker", "^NSEI")

if st.button("Run Bot"):

    df = get_data(ticker)
    df = add_indicators(df)
    df = create_target(df)
    df = train_model(df)
    df = generate_signals(df)

    st.subheader("📊 Results")
    backtest(df)

    st.subheader("📉 Chart")

    buy_signals = np.where(df['Buy'], df['Low'] * 0.98, np.nan)
    sell_signals = np.where(df['Sell'], df['High'] * 1.02, np.nan)

    apds = [
        mpf.make_addplot(df['RSI'], panel=1),
    ]

    if np.any(df['Buy']):
        apds.append(
            mpf.make_addplot(buy_signals, type='scatter', marker='^', markersize=100)
        )

    if np.any(df['Sell']):
        apds.append(
            mpf.make_addplot(sell_signals, type='scatter', marker='v', markersize=100)
        )

    fig, axlist = mpf.plot(
        df,
        type='candle',
        style='charles',
        addplot=apds,
        volume=True,
        returnfig=True
    )

    st.pyplot(fig)