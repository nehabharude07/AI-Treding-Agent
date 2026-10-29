import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

os.makedirs("models", exist_ok=True)

X = pd.DataFrame({
"open":np.random.rand(100),
"high":np.random.rand(100),
"low":np.random.rand(100),
"close":np.random.rand(100),
"volume":np.random.rand(100)
})

y = np.random.choice([-1,0,1],100)

model = RandomForestClassifier()
model.fit(X,y)

joblib.dump(model,"models/trading_model.pkl")

print("Model created successfully")