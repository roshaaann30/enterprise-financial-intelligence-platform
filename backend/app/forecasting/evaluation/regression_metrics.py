import numpy as np

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)


class RegressionMetrics:

    @staticmethod
    def evaluate(
        y_true,
        y_pred,
    ):

        y_true = np.array(
            y_true,
            dtype=np.float32,
        )

        y_pred = np.array(
            y_pred,
            dtype=np.float32,
        )

        mae = mean_absolute_error(
            y_true,
            y_pred,
        )

        rmse = np.sqrt(
            mean_squared_error(
                y_true,
                y_pred,
            )
        )

        r2 = r2_score(
            y_true,
            y_pred,
        )

        epsilon = 1e-8

        mape = np.mean(

            np.abs(

                (y_true - y_pred)

                /

                (y_true + epsilon)

            )

        ) * 100

        return {

            "MAE": mae,

            "RMSE": rmse,

            "R2": r2,

            "MAPE": mape,

        }