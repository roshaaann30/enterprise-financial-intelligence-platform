import pandas as pd

from app.forecasting.pipeline import (
    ForecastPipeline,
)

dates = pd.date_range(
    "2024-01-01",
    periods=20,
)

stock = pd.DataFrame({
    "Date": dates,
    "Close": range(20),
})

financial = pd.DataFrame({
    "Date": dates,
    "Revenue": range(100, 120),
    "EPS": [2.0 + i * 0.1 for i in range(20)],
})

macro = pd.DataFrame({
    "Date": dates,
    "FedFundsRate": [5.25] * 20,
})

news = pd.DataFrame({
    "Date": dates,
    "SentimentScore": [0.2] * 20,
})

result = ForecastPipeline.build(
    stock,
    financial,
    macro,
    news,
)

print(result["dataset"].head())
print(result["train"].shape)
print(result["validation"].shape)
print(result["test"].shape)