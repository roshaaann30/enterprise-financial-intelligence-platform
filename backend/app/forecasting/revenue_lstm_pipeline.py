import torch

from torch.utils.data import DataLoader

from app.forecasting.preprocessing.scaler import (
    ForecastScaler,
)

from app.forecasting.preprocessing.sequence_builder import (
    SequenceBuilder,
)

from app.forecasting.datasets.revenue_dataset import (
    RevenueDataset,
)

from app.forecasting.models.lstm_model import (
    RevenueLSTM,
)

from app.forecasting.trainers.lstm_trainer import (
    LSTMTrainer,
)

from app.forecasting.evaluation.regression_metrics import (
    RegressionMetrics,
)


class RevenueLSTMPipeline:

    @staticmethod
    def train(
        train_df,
        validation_df,
        params=None,
    ):

        ###########################################################
        # Default Hyperparameters
        ###########################################################

        if params is None:

            params = {}

        learning_rate = params.get(
            "learning_rate",
            0.001,
        )

        hidden_size = params.get(
            "hidden_size",
            128,
        )

        num_layers = params.get(
            "num_layers",
            2,
        )

        dropout = params.get(
            "dropout",
            0.2,
        )

        batch_size = params.get(
            "batch_size",
            32,
        )

        epochs = params.get(
            "epochs",
            50,
        )

        ###########################################################
        # Split Features and Target
        ###########################################################

        target = "Target_Revenue"

        X_train = train_df.drop(
            columns=[target]
        )

        y_train = train_df[target]

        X_validation = validation_df.drop(
            columns=[target]
        )

        y_validation = validation_df[target]

        ###########################################################
        # Scale Features
        ###########################################################

        scaler = ForecastScaler()

        X_train = scaler.fit_transform_features(
            X_train
        )

        X_validation = scaler.transform_features(
            X_validation
        )

        y_train = scaler.fit_transform_target(
            y_train
        )

        y_validation = scaler.transform_target(
            y_validation
        )

        ###########################################################
        # Save Scalers
        ###########################################################

        scaler.save()

        ###########################################################
        # Build Sequences
        ###########################################################

        X_train_seq, y_train_seq = SequenceBuilder.build(
            X_train,
            y_train,
        )

        X_validation_seq, y_validation_seq = SequenceBuilder.build(
            X_validation,
            y_validation,
        )

        ###########################################################
        # Dataset
        ###########################################################

        train_dataset = RevenueDataset(
            X_train_seq,
            y_train_seq,
        )

        validation_dataset = RevenueDataset(
            X_validation_seq,
            y_validation_seq,
        )

        ###########################################################
        # DataLoader
        ###########################################################

        train_loader = DataLoader(
            train_dataset,
            batch_size=batch_size,
            shuffle=True,
        )

        validation_loader = DataLoader(
            validation_dataset,
            batch_size=batch_size,
            shuffle=False,
        )

        ###########################################################
        # Model
        ###########################################################

        model = RevenueLSTM(

            input_size=X_train_seq.shape[2],

            hidden_size=hidden_size,

            num_layers=num_layers,

            dropout=dropout,

        )

        ###########################################################
        # Trainer
        ###########################################################

        trainer = LSTMTrainer(

            model=model,

            learning_rate=learning_rate,

            patience=5,

        )

        ###########################################################
        # Train
        ###########################################################

        history = trainer.train(

            train_loader=train_loader,

            validation_loader=validation_loader,

            epochs=epochs,

        )

        ###########################################################
        # Predict
        ###########################################################

        predictions, actuals = trainer.predict(
            validation_loader
        )

        ###########################################################
        # Convert Back
        ###########################################################

        predictions = scaler.inverse_target(
            torch.tensor(
                predictions
            ).numpy()
        )

        actuals = scaler.inverse_target(
            torch.tensor(
                actuals
            ).numpy()
        )

        ###########################################################
        # Metrics
        ###########################################################

        metrics = RegressionMetrics.evaluate(
            actuals,
            predictions,
        )

        ###########################################################
        # Return
        ###########################################################

        return {

            "model": model,

            "metrics": metrics,

            "history": history,

            "predictions": predictions,

            "actuals": actuals,

        }