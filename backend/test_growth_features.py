import pandas as pd

from app.features.pipeline import (
    FeatureEngineeringPipeline,
)

data = {
    "Revenue": [1000, 1200],
    "Gross Profit": [500, 620],
    "Operating Income": [200, 260],
    "Net Income": [150, 180],
    "EPS": [2.5, 3.0],
    "Total Assets": [1000, 1100],
    "Total Equity": [700, 760],
    "Total Debt": [300, 340],
    "Cash": [120, 150],
    "Operating Cash Flow": [180, 220],
    "Current Assets": [400, 430],
    "Current Liabilities": [200, 210],
    "Inventory": [50, 55],
    "Cost Of Revenue": [500, 580],
}

df = pd.DataFrame(data)

pipeline = FeatureEngineeringPipeline()

features = pipeline.process(df)

print(features.T)