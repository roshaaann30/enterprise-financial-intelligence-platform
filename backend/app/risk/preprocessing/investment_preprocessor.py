import joblib

from pathlib import Path

from sklearn.model_selection import (
    train_test_split,
)

from sklearn.preprocessing import (
    StandardScaler,
)

from app.risk.features.investment_features import (
    InvestmentFeatures,
)


class InvestmentPreprocessor:

    """
    Enterprise Investment Preprocessor
    """

    ###########################################################
    # Constructor
    ###########################################################

    def __init__(

        self,

        test_size=0.20,

        random_state=42,

    ):

        self.test_size = test_size

        self.random_state = random_state

        self.scaler = StandardScaler()

    ###########################################################
    # Feature Engineering
    ###########################################################

    def generate_features(

        self,

        X,

    ):

        return InvestmentFeatures.generate(

            X

        )

    ###########################################################
    # Train Test Split
    ###########################################################

    def split(

        self,

        X,

        y,

    ):

        return train_test_split(

            X,

            y,

            test_size=self.test_size,

            random_state=self.random_state,

            stratify=y,

        )

    ###########################################################
    # Scaling
    ###########################################################

    def scale(

        self,

        X_train,

        X_test,

    ):

        X_train_scaled = (

            self.scaler.fit_transform(

                X_train

            )

        )

        X_test_scaled = (

            self.scaler.transform(

                X_test

            )

        )

        return (

            X_train_scaled,

            X_test_scaled,

        )

    ###########################################################
    # Save Scaler
    ###########################################################

    def save_scaler(

        self,

        filename="investment_scaler.pkl",

    ):

        save_path = (

            Path(__file__)
            .resolve()
            .parents[3]

            / "models"

            / filename

        )

        save_path.parent.mkdir(

            exist_ok=True,

            parents=True,

        )

        joblib.dump(

            self.scaler,

            save_path,

        )

    ###########################################################
    # Load Scaler
    ###########################################################

    @staticmethod
    def load_scaler(

        filename="investment_scaler.pkl",

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

    ###########################################################
    # Class Distribution
    ###########################################################

    @staticmethod
    def class_distribution(

        y,

    ):

        counts = y.value_counts()

        percentages = (

            y.value_counts(
                normalize=True
            ) * 100

        )

        return {

            "Counts":

                counts.to_dict(),

            "Percentages":

                percentages.round(
                    2
                ).to_dict(),

        }

    ###########################################################
    # Complete Pipeline
    ###########################################################

    def process(

        self,

        X,

        y,

    ):

        #######################################################
        # Generate Features
        #######################################################

        X = self.generate_features(

            X

        )

        #######################################################
        # Split
        #######################################################

        (

            X_train,

            X_test,

            y_train,

            y_test,

        ) = self.split(

            X,

            y,

        )

        #######################################################
        # Scale
        #######################################################

        (

            X_train,

            X_test,

        ) = self.scale(

            X_train,

            X_test,

        )

        #######################################################
        # Save Scaler
        #######################################################

        self.save_scaler()

        #######################################################
        # Return
        #######################################################

        return {

            "X_train":

                X_train,

            "X_test":

                X_test,

            "y_train":

                y_train,

            "y_test":

                y_test,

            "distribution":

                self.class_distribution(
                    y
                ),

        }