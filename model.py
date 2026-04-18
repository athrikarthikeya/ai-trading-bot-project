from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def create_target(df):
    df['Return'] = df['Close'].pct_change().shift(-1)
    df['Target'] = (df['Return'] > 0.002).astype(int)
    return df

def train_model(df):
    df = df.dropna()

    X = df[['RSI', 'MACD', 'SMA', 'EMA', 'Volatility', 'Momentum']]
    y = df['Target']

    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    test_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, test_pred)
    print(f"Model Accuracy: {accuracy:.2f}")

    df['Prediction'] = model.predict(X)

    return df

def generate_signals(df):
    df['Prediction'] = df['Prediction'].fillna(0)

    df['Buy'] = (
        (df['Prediction'] == 1) &
        (df['RSI'] < 45)
    )

    df['Sell'] = (
        (df['Prediction'] == 0) |
        (df['RSI'] > 60)
    )

    return df