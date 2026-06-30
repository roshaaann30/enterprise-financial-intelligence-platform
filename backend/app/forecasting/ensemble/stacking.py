import joblib
import numpy as np
import os

from sklearn.linear_model import LinearRegression


class StackingEnsemble:

    def __init__(

        self,

    ):

        ###########################################################

        # Meta Model

        ###########################################################

        self.meta_model = LinearRegression()

    ###############################################################

    def fit(

        self,

        predictions,

        actuals,

    ):

        """
        predictions

        {

            "linear": np.array(...),

            "xgboost": np.array(...),

            "lightgbm": np.array(...),

            "catboost": np.array(...),

            "lstm": np.array(...),

            "gru": np.array(...),

            "transformer": np.array(...),

        }

        """

        ###########################################################

        # Feature Matrix

        ###########################################################

        X = np.column_stack(

            [

                predictions[key]

                for key in predictions

            ]

        )

        ###########################################################

        # Train Meta Model

        ###########################################################

        self.meta_model.fit(

            X,

            actuals,

        )

    ###############################################################

    def predict(

        self,

        predictions,

    ):

        ###########################################################

        # Feature Matrix

        ###########################################################

        X = np.column_stack(

            [

                predictions[key]

                for key in predictions

            ]

        )

        ###########################################################

        # Final Prediction

        ###########################################################

        return self.meta_model.predict(

            X

        )

    ###############################################################

    def save(

        self,

        path="app/forecasting/saved_models/stacking_meta.pkl",

    ):

        os.makedirs(

            os.path.dirname(path),

            exist_ok=True,

        )

        joblib.dump(

            self.meta_model,

            path,

        )

    ###############################################################

    def load(

        self,

        path="app/forecasting/saved_models/stacking_meta.pkl",

    ):

        self.meta_model = joblib.load(

            path

        )