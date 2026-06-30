import pandas as pd

from app.features.pipeline import (
    FeatureEngineeringPipeline,
)

data = {
    "Revenue": [1000],
    "Gross Profit": [500],
    "Operating Income": [200],
    "Net Income": [150],
    "Current Assets": [400],
    "Current Liabilities": [200],
    "Inventory": [50],
    "Total Debt": [300],
    "Total Equity": [700],
    "Total Assets": [1000],
    "Cost Of Revenue": [500],
}

df = pd.DataFrame(data)

pipeline = FeatureEngineeringPipeline()

features = pipeline.process(df)

print(features.T)