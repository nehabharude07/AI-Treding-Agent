import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# dataset load
df = pd.read_csv("F:/AI Treding Agent/data/btc_usdc.csv")

# target create
df["target"] = (df["close"].shift(-1) > df["close"]).astype(int)

df.dropna(inplace=True)

X = df[["open","high","low","close","volume"]]
y = df["target"]

model = RandomForestClassifier(n_estimators=200)

model.fit(X,y)

joblib.dump(model,"trading_model.pkl")

print("Model trained successfully")