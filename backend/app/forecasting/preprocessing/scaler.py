import joblib
import os

from sklearn.preprocessing import StandardScaler


class ForecastScaler:

    def __init__(self):

        self.feature_scaler = StandardScaler()

        self.target_scaler = StandardScaler()

    #########################################################
    # Feature Scaling
    #########################################################

    def fit_transform_features(
        self,
        dataframe,
    ):

        return self.feature_scaler.fit_transform(
            dataframe
        )

    def transform_features(
        self,
        dataframe,
    ):

        return self.feature_scaler.transform(
            dataframe
        )

    #########################################################
    # Target Scaling
    #########################################################

    def fit_transform_target(
        self,
        target,
    ):

        return self.target_scaler.fit_transform(
            target.values.reshape(-1, 1)
        ).flatten()

    def transform_target(
        self,
        target,
    ):

        return self.target_scaler.transform(
            target.values.reshape(-1, 1)
        ).flatten()

    #########################################################
    # Convert Prediction Back
    #########################################################

    def inverse_target(
        self,
        prediction,
    ):

        return self.target_scaler.inverse_transform(
            prediction.reshape(-1, 1)
        ).flatten()

    #########################################################
    # Save Scalers
    #########################################################

    def save(
        self,
        folder="app/forecasting/saved_models",
    ):

        os.makedirs(
            folder,
            exist_ok=True,
        )

        joblib.dump(

            self.feature_scaler,

            os.path.join(
                folder,
                "feature_scaler.pkl",
            ),

        )

        joblib.dump(

            self.target_scaler,

            os.path.join(
                folder,
                "target_scaler.pkl",
            ),

        )

    #########################################################
    # Load Scalers
    #########################################################

    def load(
        self,
        folder="app/forecasting/saved_models",
    ):

        self.feature_scaler = joblib.load(

            os.path.join(
                folder,
                "feature_scaler.pkl",
            )

        )

        self.target_scaler = joblib.load(

            os.path.join(
                folder,
                "target_scaler.pkl",
            )

        )