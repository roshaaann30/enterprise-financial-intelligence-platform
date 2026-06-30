import optuna

from app.risk.optimization.credit_objective import (
    CreditObjective,
)


class CreditOptimizer:

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

        study = optuna.create_study(

            direction="maximize",

            study_name="credit_risk",

        )

        study.optimize(

            lambda trial:

            CreditObjective.objective(

                trial,

                X_train,

                y_train,

                X_test,

                y_test,

            ),

            n_trials=n_trials,

        )

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