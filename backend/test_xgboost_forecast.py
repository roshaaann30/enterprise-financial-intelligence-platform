import numpy as np
import pandas as pd

from app.forecasting.revenue_xgboost_pipeline import (
    RevenueXGBoostPipeline,
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

model, metrics = RevenueXGBoostPipeline.train(

    train,

    validation,

)

print()

print("=" * 60)

print("Revenue Forecast Results")

print("=" * 60)

for key, value in metrics.items():

    print(f"{key:<10}: {value:.4f}")