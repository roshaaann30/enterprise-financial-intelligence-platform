import optuna

from app.risk.optimization.company_quality_objective import (
    CompanyQualityObjective,
)


class CompanyQualityOptimizer:

    """
    Company Quality Optuna Optimizer
    """

    @staticmethod
    def optimize(

        X_train,

        y_train,

        X_test,

        y_test,

        n_trials=20,

    ):

        study = optuna.create_study(

            direction="minimize",

            study_name="company_quality",

        )

        study.optimize(

            lambda trial:

            CompanyQualityObjective.objective(

                trial,

                X_train,

                y_train,

                X_test,

                y_test,

            ),

            n_trials=n_trials,

        )

        return {

            "best_rmse":

                float(

                    study.best_value

                ),

            "best_params":

                study.best_params,

        }