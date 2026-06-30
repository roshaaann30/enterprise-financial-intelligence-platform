from pathlib import Path

import joblib

from xgboost import XGBRegressor


class CompanyQualityModel:

    """
    Enterprise Company Quality Model
    """

    ###########################################################
    # Constructor
    ###########################################################

    def __init__(

        self,

        learning_rate=0.05,

        max_depth=4,

        n_estimators=300,

        subsample=0.8,

        colsample_bytree=0.8,

        random_state=42,

    ):

        self.model = XGBRegressor(

            objective="reg:squarederror",

            learning_rate=learning_rate,

            max_depth=max_depth,

            n_estimators=n_estimators,

            subsample=subsample,

            colsample_bytree=colsample_bytree,

            random_state=random_state,

            n_jobs=-1,

        )

    ###########################################################
    # Train
    ###########################################################

    def fit(

        self,

        X_train,

        y_train,

    ):

        self.model.fit(

            X_train,

            y_train,

        )

        return self

    ###########################################################
    # Predict
    ###########################################################

    def predict(

        self,

        X,

    ):

        return self.model.predict(

            X

        )

    ###########################################################
    # Save
    ###########################################################

    def save(

        self,

        filename="company_quality_model.pkl",

    ):

        save_path = (

            Path(__file__)
            .resolve()
            .parents[3]

            / "models"

            / filename

        )

        save_path.parent.mkdir(

            parents=True,

            exist_ok=True,

        )

        joblib.dump(

            self.model,

            save_path,

        )

    ###########################################################
    # Load
    ###########################################################

    @staticmethod
    def load(

        filename="company_quality_model.pkl",

    ):

        load_path = (

            Path(__file__)
            .resolve()
            .parents[3]

            / "models"

            / filename

        )

        return joblib.load(

            load_path

        )