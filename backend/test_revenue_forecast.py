import pandas as pd
import numpy as np

from app.forecasting.revenue_pipeline import (
    RevenueForecastPipeline,
)

rows = 100

df = pd.DataFrame({

    "Feature1": np.random.rand(rows),

    "Feature2": np.random.rand(rows),

    "Target_Revenue": np.random.rand(rows) * 1000,

})

train = df.iloc[:70]

validation = df.iloc[70:85]

model, metrics = RevenueForecastPipeline.train(
    train,
    validation,
)

print(metrics)