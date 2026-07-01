import mlflow
import random

mlflow.set_experiment(
    "EFIP Revenue Forecasting"
)

with mlflow.start_run():

    learning_rate = 0.001
    epochs = 100

    accuracy = round(
        random.uniform(0.85, 0.95),
        4
    )

    mlflow.log_param(
        "learning_rate",
        learning_rate
    )

    mlflow.log_param(
        "epochs",
        epochs
    )

    mlflow.log_metric(
        "accuracy",
        accuracy
    )

    print(
        f"Accuracy: {accuracy}"
    )