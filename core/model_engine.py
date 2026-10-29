# core/model_engine.py

import numpy as np
from sklearn.linear_model import LogisticRegression

class ModelEngine:

    def __init__(self):
        self.model = LogisticRegression()

    def train(self, df):

        X = df[["open","high","low","close","volume"]]
        y = (df["close"].shift(-1) > df["close"]).astype(int)

        self.model.fit(X[:-1], y[:-1])

    def predict(self, features):

        X = np.array([[ 
            features["open"],
            features["high"],
            features["low"],
            features["close"],
            features["volume"]
        ]])

        pred = self.model.predict(X)[0]

        if pred == 1:
            return "BUY"
        else:
            return "SELL"