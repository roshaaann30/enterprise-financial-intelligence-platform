from sklearn.metrics import (
    mean_squared_error,
)

from app.risk.models.company_quality_model import (
    CompanyQualityModel,
)


class CompanyQualityObjective:

    """
    Company Quality Objective Function
    """

    @staticmethod
    def objective(

        trial,

        X_train,

        y_train,

        X_test,

        y_test,

    ):

        model = CompanyQualityModel(

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

        rmse = (

            mean_squared_error(

                y_test,

                predictions,

            )

            ** 0.5

        )

        return float(

            rmse

        )