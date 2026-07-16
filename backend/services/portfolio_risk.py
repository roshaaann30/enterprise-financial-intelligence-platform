# backend/services/portfolio_risk.py

import numpy as np


class PortfolioRiskAnalyzer:

    def __init__(self):
        pass

    def calculate_metrics(self, returns):

        returns = np.array(returns)

        avg_return = np.mean(returns)

        volatility = np.std(returns)

        sharpe_ratio = (
            avg_return / volatility
            if volatility != 0
            else 0
        )

        cumulative = np.cumprod(1 + returns)

        peak = np.maximum.accumulate(cumulative)

        drawdown = (cumulative - peak) / peak

        max_drawdown = np.min(drawdown)

        risk_score = min(
            100,
            round(volatility * 1000)
        )

        return {
            "average_return": round(float(avg_return), 4),
            "volatility": round(float(volatility), 4),
            "sharpe_ratio": round(float(sharpe_ratio), 4),
            "max_drawdown": round(float(max_drawdown), 4),
            "risk_score": risk_score
        }