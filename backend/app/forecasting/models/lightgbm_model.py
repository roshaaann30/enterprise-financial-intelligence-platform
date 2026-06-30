import os
import joblib

from lightgbm import LGBMRegressor


class RevenueLightGBM:

    def __init__(self):

        self.model = LGBMRegressor(

            n_estimators=500,

            learning_rate=0.03,

            max_depth=8,

            subsample=0.8,

            colsample_bytree=0.8,

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