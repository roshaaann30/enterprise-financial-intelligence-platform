import numpy as np
import pandas as pd

from app.forecasting.revenue_ensemble_pipeline import (
    RevenueEnsemblePipeline,
)

##############################################################
# Simulated Predictions
##############################################################

np.random.seed(42)

samples = 100

actuals = np.random.uniform(

    1000,

    5000,

    samples,

)

predictions = {

    "linear":

        actuals + np.random.normal(0,180,samples),

    "xgboost":

        actuals + np.random.normal(0,140,samples),

    "lightgbm":

        actuals + np.random.normal(0,120,samples),

    "catboost":

        actuals + np.random.normal(0,110,samples),

    "lstm":

        actuals + np.random.normal(0,90,samples),

    "gru":

        actuals + np.random.normal(0,80,samples),

    "transformer":

        actuals + np.random.normal(0,60,samples),

}

##############################################################
# Run Ensemble
##############################################################

results = RevenueEnsemblePipeline.evaluate(

    predictions,

    actuals,

)

##############################################################
# Leaderboard
##############################################################

leaderboard = []

for model, metrics in results["leaderboard"].items():

    leaderboard.append({

        "Model": model,

        "MAE": metrics["MAE"],

        "RMSE": metrics["RMSE"],

        "MAPE": metrics["MAPE"],

        "R2": metrics["R2"],

    })

leaderboard = pd.DataFrame(

    leaderboard

)

leaderboard = leaderboard.sort_values(

    "RMSE"

)

##############################################################
# Save CSV
##############################################################

leaderboard.to_csv(

    "app/forecasting/saved_models/ensemble_leaderboard.csv",

    index=False,

)

##############################################################
# Print
##############################################################

print()

print("="*80)

print("ENTERPRISE ENSEMBLE LEADERBOARD")

print("="*80)

print(leaderboard)

print()

print("="*80)

print("BEST MODEL")

print("="*80)

print(

    leaderboard.iloc[0]["Model"]

)

print()

print("="*80)

print("Saved")

print("="*80)

print(

    "ensemble_leaderboard.csv"

)