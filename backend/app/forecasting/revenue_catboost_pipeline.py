from app.forecasting.models.catboost_model import (
    RevenueCatBoost,
)

from app.forecasting.evaluation.regression_metrics import (
    RegressionMetrics,
)


class RevenueCatBoostPipeline:

    @staticmethod
    def train(
        train_df,
        validation_df,
    ):

        target = "Target_Revenue"

        X_train = train_df.drop(
            columns=[target]
        )

        y_train = train_df[target]

        X_valid = validation_df.drop(
            columns=[target]
        )

        y_valid = validation_df[target]

        model = RevenueCatBoost()

        model.train(
            X_train,
            y_train,
        )

        predictions = model.predict(
            X_valid
        )

        metrics = RegressionMetrics.evaluate(
            y_valid,
            predictions,
        )

        model.save(
            "app/forecasting/saved_models/revenue_catboost.pkl"
        )

        return model, metrics