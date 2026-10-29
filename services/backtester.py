import pandas as pd
import numpy as np

class Backtester:

    def run(self, df):

        # price returns
        df["returns"] = df["close"].pct_change()

        # strategy returns
        df["strategy_returns"] = df["signal"].shift(1) * df["returns"]

        df = df.dropna()

        returns = df["strategy_returns"]

        # equity curve
        equity_curve = (1 + returns).cumprod()

        # ===== Metrics =====

        sharpe = np.sqrt(252) * returns.mean() / (returns.std() + 1e-9)

        downside = returns[returns < 0]
        sortino = np.sqrt(252) * returns.mean() / (downside.std() + 1e-9) if len(downside) > 0 else 0

        cumulative = (1 + returns).cumprod()
        peak = cumulative.cummax()
        drawdown = (cumulative - peak) / peak
        max_drawdown = drawdown.min()

        win_rate = (returns > 0).sum() / len(returns)

        volatility = returns.std() * np.sqrt(252)

        total_return = equity_curve.iloc[-1] - 1

        metrics = {
            "sharpe_ratio": float(sharpe),
            "sortino_ratio": float(sortino),
            "max_drawdown": float(max_drawdown),
            "win_rate": float(win_rate),
            "volatility": float(volatility),
            "total_return": float(total_return)
        }

        return equity_curve, returns, metrics