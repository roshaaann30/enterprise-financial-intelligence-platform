from sklearn.metrics import (
    roc_auc_score,
    mean_squared_error,
)

from app.risk.models.investment_risk_model import (
    InvestmentRiskModel,
)

from app.risk.models.return_prediction_model import (
    ReturnPredictionModel,
)


class InvestmentObjective:

    ###########################################################
    # Risk Model Objective
    ###########################################################

    @staticmethod
    def risk_objective(

        trial,

        X_train,

        y_train,

        X_test,

        y_test,

    ):

        model = InvestmentRiskModel(

            learning_rate=trial.suggest_float(
                "learning_rate",
                0.001,
                0.2,
                log=True,
            ),

            max_depth=trial.suggest_int(
                "max_depth",
                3,
                10,
            ),

            n_estimators=trial.suggest_int(
                "n_estimators",
                100,
                1000,
            ),

            subsample=trial.suggest_float(
                "subsample",
                0.5,
                1.0,
            ),

            colsample_bytree=trial.suggest_float(
                "colsample_bytree",
                0.5,
                1.0,
            ),

        )

        model.fit(
            X_train,
            y_train,
        )

        probabilities = model.predict_proba(
            X_test
        )

        score = roc_auc_score(
            y_test,
            probabilities,
        )

        return float(score)

    ###########################################################
    # Return Model Objective
    ###########################################################

    @staticmethod
    def return_objective(

        trial,

        X_train,

        y_train,

        X_test,

        y_test,

    ):

        model = ReturnPredictionModel(

            learning_rate=trial.suggest_float(
                "learning_rate",
                0.001,
                0.2,
                log=True,
            ),

            max_depth=trial.suggest_int(
                "max_depth",
                3,
                10,
            ),

            n_estimators=trial.suggest_int(
                "n_estimators",
                100,
                1000,
            ),

            subsample=trial.suggest_float(
                "subsample",
                0.5,
                1.0,
            ),

            colsample_bytree=trial.suggest_float(
                "colsample_bytree",
                0.5,
                1.0,
            ),

        )

        model.fit(
            X_train,
            y_train,
        )

        predictions = model.predict(
            X_test
        )

        rmse = mean_squared_error(
            y_test,
            predictions,
            squared=False,
        )

        return float(rmse)