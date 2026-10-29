import os
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware

import pandas as pd
import numpy as np
import joblib

# =========================
# APP INIT
# =========================
app = FastAPI(title="AI Trust Trading Agent")

# =========================
# CORS CONFIGURATION
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# PATH CONFIGURATION
# =========================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Project root

STATIC_DIR = os.path.join(BASE_DIR, "frontend", "static")
TEMPLATE_DIR = os.path.join(BASE_DIR, "frontend", "templates")

if not os.path.exists(STATIC_DIR):
    raise RuntimeError(f"Directory '{STATIC_DIR}' does not exist. Create it!")
if not os.path.exists(TEMPLATE_DIR):
    raise RuntimeError(f"Directory '{TEMPLATE_DIR}' does not exist. Create it!")

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
templates = Jinja2Templates(directory=TEMPLATE_DIR)

# =========================
# LOAD MODEL
# =========================
MODEL_PATH = os.path.join(BASE_DIR, "models", "trading_model.pkl")
if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    model = None
    print("⚠️ Warning: Model file not found at", MODEL_PATH)

# =========================
# TRADE HISTORY STORAGE
# =========================
trade_history = []

# =========================
# HOME PAGE
# =========================
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
    request=request,
    name="index.html"
)

# =========================
# RUN AGENT ENDPOINT
# =========================
@app.post("/run-agent")
async def run_agent(data: dict):
    if model is None:
        return JSONResponse({"error": "Trading model not loaded"}, status_code=500)

    try:
        portfolio_value = float(data.get("portfolio_value", 0))
        trade_size = float(data.get("trade_size", 0))
        features = data.get("features", {})

        open_price = float(features.get("open", 0))
        high_price = float(features.get("high", 0))
        low_price = float(features.get("low", 0))
        close_price = float(features.get("close", 0))
        volume = float(features.get("volume", 0))

        X = pd.DataFrame([{
            "open": open_price,
            "high": high_price,
            "low": low_price,
            "close": close_price,
            "volume": volume
        }])

        prediction = model.predict(X)[0]

        signal = "HOLD"
        if prediction == 1:
            signal = "BUY"
        elif prediction == -1:
            signal = "SELL"

        position_size = trade_size * 0.1
        profit = 0
        if signal == "BUY":
            profit = (close_price - open_price) * position_size
        elif signal == "SELL":
            profit = (open_price - close_price) * position_size

        trade_history.append(profit)

        return {
            "signal": signal,
            "profit": round(profit, 2),
            "position_size": round(position_size, 2)
        }

    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=400)

# =========================
# METRICS ENDPOINT
# =========================
@app.get("/metrics")
async def metrics():
    if len(trade_history) == 0:
        return {"total_trades": 0, "profit": 0.0, "win_rate": 0.0}

    returns = np.array(trade_history)
    return {
        "total_trades": len(returns),
        "profit": float(returns.sum()),
        "win_rate": float((returns > 0).mean())
    }