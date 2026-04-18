from data import get_data
from indicators import add_indicators
from model import create_target, train_model, generate_signals
from visualize import plot_chart
from backtest import backtest

df = get_data("^NSEI")

df = add_indicators(df)

df = create_target(df)

df = train_model(df)

df = generate_signals(df)

backtest(df)

plot_chart(df)