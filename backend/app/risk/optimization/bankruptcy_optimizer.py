import optuna

from app.risk.optimization.bankruptcy_objective import (
    BankruptcyObjective,
)


class BankruptcyOptimizer:

    ###########################################################
    # Optimize
    ###########################################################

    @staticmethod
    def optimize(

        X_train,

        y_train,

        X_test,

        y_test,

        n_trials=25,

    ):

        #######################################################
        # Study
        #######################################################

        study = optuna.create_study(

            direction="maximize",

            study_name="bankruptcy_xgboost",

        )

        #######################################################
        # Objective
        #######################################################

        study.optimize(

            lambda trial:

            BankruptcyObjective.objective(

                trial,

                X_train,

                y_train,

                X_test,

                y_test,

            ),

            n_trials=n_trials,

        )

        #######################################################
        # Results
        #######################################################

        return {

            "best_score":

                float(

                    study.best_value

                ),

            "best_params":

                study.best_params,

            "study":

                study,

        }