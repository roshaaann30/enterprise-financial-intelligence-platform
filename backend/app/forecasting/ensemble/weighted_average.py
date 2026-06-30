import numpy as np


class WeightedAverageEnsemble:

    def __init__(

        self,

        weights=None,

    ):

        ###########################################################
        # Default Weights
        ###########################################################

        if weights is None:

            self.weights = {

                "linear": 0.05,

                "xgboost": 0.05,

                "lightgbm": 0.10,

                "catboost": 0.10,

                "lstm": 0.20,

                "gru": 0.20,

                "transformer": 0.30,

            }

        else:

            self.weights = weights

    ###############################################################

    def predict(

        self,

        predictions,

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

        # Validation

        ###########################################################

        missing_models = [

            model

            for model in self.weights

            if model not in predictions

        ]

        if missing_models:

            raise ValueError(

                f"Missing predictions for: {missing_models}"

            )

        ###########################################################

        # Weighted Prediction

        ###########################################################

        ensemble_prediction = np.zeros_like(

            predictions["transformer"],

            dtype=np.float64,

        )

        for model_name, weight in self.weights.items():

            ensemble_prediction += (

                predictions[model_name]

                * weight

            )

        return ensemble_prediction

    ###############################################################

    def update_weights(

        self,

        new_weights,

    ):

        total_weight = sum(

            new_weights.values()

        )

        if abs(total_weight - 1.0) > 1e-6:

            raise ValueError(

                "Weights must sum to 1.0"

            )

        self.weights = new_weights

    ###############################################################

    def get_weights(

        self,

    ):

        return self.weights