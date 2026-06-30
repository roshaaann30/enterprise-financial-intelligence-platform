import os
import joblib

from catboost import CatBoostRegressor


class RevenueCatBoost:

    def __init__(self):

        self.model = CatBoostRegressor(

            iterations=500,

            learning_rate=0.03,

            depth=8,

            loss_function="RMSE",

            random_seed=42,

            verbose=False,

        )

    def train(
        self,
        X_train,
        y_train,
    ):

        self.model.fit(
            X_train,
            y_train,
        )

    def predict(
        self,
        X,
    ):

        return self.model.predict(X)

    def save(
        self,
        path,
    ):

        os.makedirs(
            os.path.dirname(path),
            exist_ok=True,
        )

        joblib.dump(
            self.model,
            path,
        )

    def load(
        self,
        path,
    ):

        self.model = joblib.load(path)