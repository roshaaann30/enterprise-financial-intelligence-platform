import os
import joblib

from xgboost import XGBRegressor


class RevenueXGBoost:

    def __init__(self):

        self.model = XGBRegressor(

            n_estimators=300,

            learning_rate=0.05,

            max_depth=6,

            subsample=0.8,

            colsample_bytree=0.8,

            objective="reg:squarederror",

            random_state=42,

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