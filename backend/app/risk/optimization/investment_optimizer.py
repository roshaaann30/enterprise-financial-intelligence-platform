import optuna

from app.risk.optimization.investment_objective import (
    InvestmentObjective,
)


class InvestmentOptimizer:

    ###########################################################
    # Risk Optimization
    ###########################################################

    @staticmethod
    def optimize_risk(

        X_train,
        y_train,
        X_test,
        y_test,
        n_trials=20,

    ):

        study = optuna.create_study(
            direction="maximize",
            study_name="investment_risk",
        )

        study.optimize(

            lambda trial:

            InvestmentObjective.risk_objective(

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
                float(study.best_value),

            "best_params":
                study.best_params,

        }

    ###########################################################
    # Return Optimization
    ###########################################################

    @staticmethod
    def optimize_return(

        X_train,
        y_train,
        X_test,
        y_test,
        n_trials=20,

    ):

        study = optuna.create_study(
            direction="minimize",
            study_name="return_prediction",
        )

        study.optimize(

            lambda trial:

            InvestmentObjective.return_objective(

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
                float(study.best_value),

            "best_params":
                study.best_params,

        }