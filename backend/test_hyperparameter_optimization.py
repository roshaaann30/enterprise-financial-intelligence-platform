import numpy as np
import pandas as pd

from app.forecasting.revenue_hyperparameter_pipeline import (
    RevenueHyperparameterPipeline,
)

from app.forecasting.revenue_lstm_pipeline import (
    RevenueLSTMPipeline,
)

############################################################
# Sample Dataset
############################################################

np.random.seed(42)

rows = 400

df = pd.DataFrame({

    "Revenue": np.random.rand(rows) * 1000,

    "EPS": np.random.rand(rows) * 20,

    "DebtRatio": np.random.rand(rows),

    "OperatingMargin": np.random.rand(rows),

    "GDP": np.random.rand(rows) * 30000,

    "Target_Revenue": np.random.rand(rows) * 1000,

})

############################################################
# Train / Validation Split
############################################################

train = df.iloc[:300]

validation = df.iloc[300:]

############################################################
# Run Optimization
############################################################

results = RevenueHyperparameterPipeline.optimize_lstm(

    train_df=train,

    validation_df=validation,

    pipeline=RevenueLSTMPipeline,

    n_trials=20,

)

############################################################
# Print Results
############################################################

print()

print("=" * 70)

print("OPTIMIZATION COMPLETE")

print("=" * 70)

print()

print("Best Score")

print(results["best_score"])

print()

print("Best Parameters")

for key, value in results["best_params"].items():

    print(f"{key:<20}{value}")

############################################################
# Save Best Parameters
############################################################

best = pd.DataFrame(

    [results["best_params"]]

)

best["BestScore"] = results["best_score"]

best.to_csv(

    "app/forecasting/saved_models/best_lstm_parameters.csv",

    index=False,

)

print()

print("=" * 70)

print("Saved")

print("=" * 70)

print("best_lstm_parameters.csv")