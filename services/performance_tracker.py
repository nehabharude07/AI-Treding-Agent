import numpy as np

class PerformanceTracker:

    def __init__(self):
        self.returns = []
        self.equity_curve = [10000]

    def record_trade(self, trade_size):
        pnl = np.random.uniform(-0.02, 0.03)
        self.returns.append(pnl)

        new_equity = self.equity_curve[-1] * (1 + pnl)
        self.equity_curve.append(new_equity)

    def current_drawdown(self):
        peak = max(self.equity_curve)
        current = self.equity_curve[-1]
        return (peak - current) / peak

    def sharpe_ratio(self):
        if len(self.returns) < 2:
            return 0
        return np.mean(self.returns) / np.std(self.returns)

    def metrics(self):
        return {
            "sharpe": self.sharpe_ratio(),
            "drawdown": self.current_drawdown(),
            "equity": self.equity_curve[-1]
        }