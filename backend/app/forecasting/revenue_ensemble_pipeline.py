import numpy as np

from app.forecasting.ensemble.weighted_average import (
    WeightedAverageEnsemble,
)

from app.forecasting.ensemble.voting import (
    VotingEnsemble,
)

from app.forecasting.ensemble.stacking import (
    StackingEnsemble,
)

from app.forecasting.evaluation.regression_metrics import (
    RegressionMetrics,
)


class RevenueEnsemblePipeline:

    @staticmethod
    def evaluate(

        predictions,

        actuals,

    ):

        ##########################################################
        # Weighted Average
        ##########################################################

        weighted = WeightedAverageEnsemble()

        weighted_prediction = weighted.predict(

            predictions

        )

        ##########################################################
        # Voting Mean
        ##########################################################

        voting = VotingEnsemble(

            strategy="mean"

        )

        voting_prediction = voting.predict(

            predictions

        )

        ##########################################################
        # Stacking
        ##########################################################

        stacking = StackingEnsemble()

        stacking.fit(

            predictions,

            actuals,

        )

        stacking_prediction = stacking.predict(

            predictions

        )

        ##########################################################
        # Save Meta Model
        ##########################################################

        stacking.save()

        ##########################################################
        # Evaluate
        ##########################################################

        leaderboard = {

            "WeightedAverage":

                RegressionMetrics.evaluate(

                    actuals,

                    weighted_prediction,

                ),

            "Voting":

                RegressionMetrics.evaluate(

                    actuals,

                    voting_prediction,

                ),

            "Stacking":

                RegressionMetrics.evaluate(

                    actuals,

                    stacking_prediction,

                ),

        }

        ##########################################################
        # Return
        ##########################################################

        return {

            "leaderboard": leaderboard,

            "weighted_prediction": weighted_prediction,

            "voting_prediction": voting_prediction,

            "stacking_prediction": stacking_prediction,

        }