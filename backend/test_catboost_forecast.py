import numpy as np
import pandas as pd

from app.forecasting.revenue_catboost_pipeline import (
    RevenueCatBoostPipeline,
)

rows = 500

df = pd.DataFrame({

    "Feature1": np.random.rand(rows),

    "Feature2": np.random.rand(rows),

    "Feature3": np.random.rand(rows),

    "Feature4": np.random.rand(rows),

    "Target_Revenue": np.random.rand(rows) * 1000,

})

train = df.iloc[:350]

validation = df.iloc[350:425]

model, metrics = RevenueCatBoostPipeline.train(

    train,

    validation,

)

print()

print("=" * 60)

print("CatBoost Revenue Forecast")

print("=" * 60)

for metric, value in metrics.items():

    print(f"{metric:<10}: {value:.4f}")