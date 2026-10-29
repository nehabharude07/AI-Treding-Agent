import yfinance as yf

def get_live_features(symbol="AAPL"):

    data = yf.download(
        tickers=symbol,
        period="1d",
        interval="1m"
    )

    latest = data.iloc[-1]

    return {
        "open": float(latest["Open"]),
        "high": float(latest["High"]),
        "low": float(latest["Low"]),
        "close": float(latest["Close"]),
        "volume": float(latest["Volume"])
    }