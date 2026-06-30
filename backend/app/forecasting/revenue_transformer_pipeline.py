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

from app.forecasting.models.transformer_model import (
    RevenueTransformer,
)

from app.forecasting.trainers.transformer_trainer import (
    TransformerTrainer,
)

from app.forecasting.evaluation.regression_metrics import (
    RegressionMetrics,
)


class RevenueTransformerPipeline:

    @staticmethod
    def train(
        train_df,
        validation_df,
    ):

        ##########################################################
        # Target Column
        ##########################################################

        target = "Target_Revenue"

        ##########################################################
        # Split Features & Target
        ##########################################################

        X_train = train_df.drop(
            columns=[target]
        )

        y_train = train_df[target]

        X_validation = validation_df.drop(
            columns=[target]
        )

        y_validation = validation_df[target]

        ##########################################################
        # Scale Features
        ##########################################################

        scaler = ForecastScaler()

        X_train = scaler.fit_transform_features(
            X_train
        )

        X_validation = scaler.transform_features(
            X_validation
        )

        ##########################################################
        # Scale Target
        ##########################################################

        y_train = scaler.fit_transform_target(
            y_train
        )

        y_validation = scaler.transform_target(
            y_validation
        )

        ##########################################################
        # Save Scalers
        ##########################################################

        scaler.save()

        ##########################################################
        # Build Sequences
        ##########################################################

        X_train_seq, y_train_seq = SequenceBuilder.build(
            X_train,
            y_train,
        )

        X_validation_seq, y_validation_seq = SequenceBuilder.build(
            X_validation,
            y_validation,
        )

        ##########################################################
        # Dataset
        ##########################################################

        train_dataset = RevenueDataset(
            X_train_seq,
            y_train_seq,
        )

        validation_dataset = RevenueDataset(
            X_validation_seq,
            y_validation_seq,
        )

        ##########################################################
        # DataLoader
        ##########################################################

        train_loader = DataLoader(

            train_dataset,

            batch_size=32,

            shuffle=True,

        )

        validation_loader = DataLoader(

            validation_dataset,

            batch_size=32,

            shuffle=False,

        )

        ##########################################################
        # Transformer Model
        ##########################################################

        model = RevenueTransformer(

            input_size=X_train_seq.shape[2],

            d_model=128,

            nhead=8,

            num_layers=4,

            dim_feedforward=256,

            dropout=0.2,

        )

        ##########################################################
        # Trainer
        ##########################################################

        trainer = TransformerTrainer(

            model=model,

            learning_rate=0.0001,

            patience=7,

        )

        ##########################################################
        # Train Model
        ##########################################################

        history = trainer.train(

            train_loader=train_loader,

            validation_loader=validation_loader,

            epochs=60,

        )

        ##########################################################
        # Predict
        ##########################################################

        predictions, actuals = trainer.predict(

            validation_loader

        )

        ##########################################################
        # Convert Predictions Back
        ##########################################################

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

        ##########################################################
        # Metrics
        ##########################################################

        metrics = RegressionMetrics.evaluate(

            actuals,

            predictions,

        )

        ##########################################################
        # Return Results
        ##########################################################

        return {

            "model": model,

            "metrics": metrics,

            "history": history,

            "predictions": predictions,

            "actuals": actuals,

        }