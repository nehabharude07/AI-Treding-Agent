import pandas as pd

class StrategyEngine:

    def generate_signals(self, df):

        df["ma_fast"] = df["close"].rolling(5).mean()
        df["ma_slow"] = df["close"].rolling(20).mean()

        df["signal"] = 0

        df.loc[df["ma_fast"] > df["ma_slow"], "signal"] = 1
        df.loc[df["ma_fast"] < df["ma_slow"], "signal"] = -1

        df = df.dropna()

        return df