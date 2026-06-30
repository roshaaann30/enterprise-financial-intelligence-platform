import numpy as np


class VotingEnsemble:

    def __init__(

        self,

        strategy="mean",

    ):

        """
        strategy

        mean

        median

        """

        self.strategy = strategy

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

        if len(predictions) == 0:

            raise ValueError(

                "No predictions supplied."

            )

        ###########################################################

        # Stack Predictions

        ###########################################################

        prediction_matrix = np.column_stack(

            [

                predictions[key]

                for key in predictions

            ]

        )

        ###########################################################

        # Mean Voting

        ###########################################################

        if self.strategy == "mean":

            return np.mean(

                prediction_matrix,

                axis=1,

            )

        ###########################################################

        # Median Voting

        ###########################################################

        elif self.strategy == "median":

            return np.median(

                prediction_matrix,

                axis=1,

            )

        ###########################################################

        # Invalid Strategy

        ###########################################################

        else:

            raise ValueError(

                f"Unknown strategy: {self.strategy}"

            )

    ###############################################################

    def set_strategy(

        self,

        strategy,

    ):

        if strategy not in [

            "mean",

            "median",

        ]:

            raise ValueError(

                "Strategy must be "

                "'mean' or 'median'."

            )

        self.strategy = strategy

    ###############################################################

    def get_strategy(

        self,

    ):

        return self.strategy