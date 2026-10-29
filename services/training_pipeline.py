import pandas as pd
from core.strategy_engine import StrategyEngine
from services.backtester import Backtester
from utils.metrics import performance_summary


def run_full_backtest():

    df = pd.read_csv("data/btc_usdc.csv")

    print("DATA LOADED:", df.head())

    strategy = StrategyEngine()

    df = strategy.generate_signals(df)

    print("SIGNALS:", df["signal"].value_counts())

    backtester = Backtester()

    equity_curve, returns = backtester.run(df)

    print("RETURNS:", returns.head())

    metrics = performance_summary(returns, equity_curve)

    return metrics, equity_curve