import pandas as pd
import numpy as np

from app.forecasting.revenue_lstm_pipeline import (
    RevenueLSTMPipeline,
)

from app.forecasting.visualization.training_visualizer import (
    TrainingVisualizer,
)

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

train = df.iloc[:280]

validation = df.iloc[280:340]

result = RevenueLSTMPipeline.train(

    train,

    validation,

)

print()

print("=" * 60)

print("Enterprise LSTM Forecast")

print("=" * 60)

for metric, value in result["metrics"].items():

    print(

        f"{metric:<10}: {value:.4f}"

    )

TrainingVisualizer.plot_loss(

    result["history"]

)

TrainingVisualizer.plot_predictions(

    result["actuals"],

    result["predictions"],

)

history = pd.DataFrame(

    result["history"]

)

history.to_csv(

    "app/forecasting/saved_models/training_history.csv",

    index=False,

)

metrics = pd.DataFrame(

    [result["metrics"]]

)

metrics.to_csv(

    "app/forecasting/saved_models/metrics.csv",

    index=False,

)

print()

print("=" * 60)

print("Files Generated")

print("=" * 60)

print("✔ revenue_lstm.pt")

print("✔ feature_scaler.pkl")

print("✔ target_scaler.pkl")

print("✔ training_history.csv")

print("✔ metrics.csv")

print("✔ training_loss.png")

print("✔ predictions.png")