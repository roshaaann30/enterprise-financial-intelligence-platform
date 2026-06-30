from pathlib import Path

import joblib

from xgboost import XGBClassifier


class CreditRiskModel:

    """
    Enterprise Credit Risk Model
    """

    ###########################################################
    # Constructor
    ###########################################################

    def __init__(

        self,

        learning_rate=0.05,

        max_depth=6,

        n_estimators=300,

        subsample=0.8,

        colsample_bytree=0.8,

        random_state=42,

    ):

        self.model = XGBClassifier(

            objective="binary:logistic",

            eval_metric="logloss",

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
    # Predict Probability
    ###########################################################

    def predict_proba(

        self,

        X,

    ):

        return self.model.predict_proba(

            X

        )[:, 1]

    ###########################################################
    # Feature Importance
    ###########################################################

    def feature_importance(

        self,

        feature_names=None,

    ):

        importance = self.model.feature_importances_

        if feature_names is None:

            feature_names = [

                f"Feature_{i}"

                for i in range(

                    len(importance)

                )

            ]

        results = []

        for name, score in zip(

            feature_names,

            importance,

        ):

            results.append(

                {

                    "Feature": name,

                    "Importance": float(score),

                }

            )

        results = sorted(

            results,

            key=lambda x: x["Importance"],

            reverse=True,

        )

        return results

    ###########################################################
    # Save Model
    ###########################################################

    def save(

        self,

        filename="credit_risk_model.pkl",

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
    # Load Model
    ###########################################################

    @staticmethod
    def load(

        filename="credit_risk_model.pkl",

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