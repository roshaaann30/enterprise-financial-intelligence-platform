import numpy as np
import pandas as pd

from app.forecasting.revenue_transformer_pipeline import (
    RevenueTransformerPipeline,
)

from app.forecasting.visualization.training_visualizer import (
    TrainingVisualizer,
)

############################################################
# Generate Sample Dataset
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

train = df.iloc[:280]

validation = df.iloc[280:340]

############################################################
# Train Transformer
############################################################

result = RevenueTransformerPipeline.train(

    train,

    validation,

)

############################################################
# Print Metrics
############################################################

print()

print("=" * 60)

print("Enterprise Transformer Forecast")

print("=" * 60)

for metric, value in result["metrics"].items():

    print(

        f"{metric:<10}: {value:.4f}"

    )

############################################################
# Plot Training History
############################################################

TrainingVisualizer.plot_loss(

    result["history"]

)

############################################################
# Plot Predictions
############################################################

TrainingVisualizer.plot_predictions(

    result["actuals"],

    result["predictions"],

)

############################################################
# Save History
############################################################

history = pd.DataFrame(

    result["history"]

)

history.to_csv(

    "app/forecasting/saved_models/transformer_training_history.csv",

    index=False,

)

############################################################
# Save Metrics
############################################################

metrics = pd.DataFrame(

    [result["metrics"]]

)

metrics.to_csv(

    "app/forecasting/saved_models/transformer_metrics.csv",

    index=False,

)

############################################################
# Finished
############################################################

print()

print("=" * 60)

print("Files Generated")

print("=" * 60)

print("✔ revenue_transformer.pt")

print("✔ feature_scaler.pkl")

print("✔ target_scaler.pkl")

print("✔ transformer_training_history.csv")

print("✔ transformer_metrics.csv")

print("✔ training_loss.png")

print("✔ predictions.png")