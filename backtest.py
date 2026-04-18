import streamlit as st

def backtest(df, initial_balance=10000):
    balance = initial_balance
    position = 0
    trades = 0

    for i in range(len(df)):
        if df['Buy'].iloc[i] and position == 0:
            buy_price = df['Close'].iloc[i]
            position = balance / buy_price
            balance = 0
            trades += 1

        elif df['Sell'].iloc[i] and position > 0:
            sell_price = df['Close'].iloc[i]
            balance = position * sell_price
            position = 0

    if position > 0:
        balance = position * df['Close'].iloc[-1]

    profit = balance - initial_balance

    st.write(f"💰 Final Balance: {balance:.2f}")
    st.write(f"📈 Profit/Loss: {profit:.2f}")
    st.write(f"🔄 Total Trades: {trades}")