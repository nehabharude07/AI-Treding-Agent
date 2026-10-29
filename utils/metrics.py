import numpy as np

def performance_summary(returns, equity_curve):

    if len(returns) == 0:
        return {
            "sharpe_ratio": 0,
            "sortino_ratio": 0,
            "max_drawdown": 0,
            "win_rate": 0,
            "volatility": 0,
            "calmar_ratio": 0,
            "profit_factor": 0,
            "total_return": 0
        }

    sharpe = np.mean(returns) / np.std(returns) * np.sqrt(252)

    win_rate = (returns > 0).sum() / len(returns)

    total_return = equity_curve.iloc[-1] - 1

    max_drawdown = (equity_curve.cummax() - equity_curve).max()

    return {
        "sharpe_ratio": float(sharpe),
        "sortino_ratio": float(sharpe),
        "max_drawdown": float(max_drawdown),
        "win_rate": float(win_rate),
        "volatility": float(np.std(returns)),
        "calmar_ratio": float(total_return / max_drawdown) if max_drawdown != 0 else 0,
        "profit_factor": float(returns[returns > 0].sum() / abs(returns[returns < 0].sum())) if (returns < 0).sum() != 0 else 0,
        "total_return": float(total_return)
    }