import pandas as pd

from app.features.financial.pipeline import (
    FinancialPipeline,
)

data = {
    "Revenue": [1000, 1200],
    "Gross Profit": [500, 620],
    "Operating Income": [200, 260],
    "Net Income": [150, 180],
    "EPS": [2.5, 3.0],
    "Current Assets": [400, 430],
    "Current Liabilities": [200, 210],
    "Inventory": [50, 55],
    "Total Debt": [300, 340],
    "Total Equity": [700, 760],
    "Total Assets": [1000, 1100],
    "Cost Of Revenue": [500, 580],
    "Cash": [120, 150],
    "Operating Cash Flow": [180, 220],
}

df = pd.DataFrame(data)

features = FinancialPipeline.process(df)

print(features.columns)