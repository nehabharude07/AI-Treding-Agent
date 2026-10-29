from services.market_data import get_live_price
import pandas as pd
import joblib

model = joblib.load("models/trading_model.pkl")

def run_realtime_trade():

    features = get_live_price("AAPL")

    X = pd.DataFrame([features])

    prediction = model.predict(X)[0]

    if prediction == 1:
        signal = "BUY"
    elif prediction == -1:
        signal = "SELL"
    else:
        signal = "HOLD"

    return {
        "features": features,
        "signal": signal
    }