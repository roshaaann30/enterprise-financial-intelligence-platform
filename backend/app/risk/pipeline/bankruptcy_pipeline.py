from app.risk.models.bankruptcy_model import (
    BankruptcyModel,
)

from app.risk.preprocessing.bankruptcy_preprocessor import (
    BankruptcyPreprocessor,
)


class BankruptcyPipeline:

    """
    Enterprise Bankruptcy Prediction Pipeline
    """

    ###########################################################
    # Risk Classification
    ###########################################################

    @staticmethod
    def classify_risk(
        probability,
    ):

        if probability < 0.10:
            return "Low"

        elif probability < 0.30:
            return "Moderate"

        elif probability < 0.60:
            return "High"

        else:
            return "Critical"

    ###########################################################
    # Confidence Score
    ###########################################################

    @staticmethod
    def confidence(
        probability,
    ):

        distance = abs(
            probability - 0.5
        )

        return min(
            1.0,
            distance * 2,
        )

    ###########################################################
    # Single Prediction
    ###########################################################

    @staticmethod
    def predict(
        features,
        model_path="bankruptcy_model.pkl",
    ):

        #######################################################
        # Load Model
        #######################################################

        model = BankruptcyModel.load(
            model_path
        )

        #######################################################
        # Load Scaler
        #######################################################

        scaler = BankruptcyPreprocessor.load_scaler()

        #######################################################
        # Scale Features
        #######################################################

        scaled_features = scaler.transform(
            features
        )

        #######################################################
        # Predict Probability
        #######################################################

        probability = float(
            model.predict_proba(
                scaled_features
            )[0][1]
        )

        #######################################################
        # Risk Level
        #######################################################

        risk = BankruptcyPipeline.classify_risk(
            probability
        )

        #######################################################
        # Confidence
        #######################################################

        confidence = BankruptcyPipeline.confidence(
            probability
        )

        #######################################################
        # Return
        #######################################################

        return {

            "bankruptcy_probability":
                probability,

            "bankruptcy_percentage":
                round(
                    probability * 100,
                    2,
                ),

            "risk_level":
                risk,

            "confidence":
                round(
                    confidence * 100,
                    2,
                ),

        }

    ###########################################################
    # Batch Prediction
    ###########################################################

    @staticmethod
    def predict_batch(
        dataframe,
        model_path="bankruptcy_model.pkl",
    ):

        #######################################################
        # Load Model
        #######################################################

        model = BankruptcyModel.load(
            model_path
        )

        #######################################################
        # Load Scaler
        #######################################################

        scaler = BankruptcyPreprocessor.load_scaler()

        #######################################################
        # Scale Features
        #######################################################

        scaled = scaler.transform(
            dataframe
        )

        #######################################################
        # Predict Probabilities
        #######################################################

        probabilities = model.predict_proba(
            scaled
        )

        #######################################################
        # Build Results
        #######################################################

        results = []

        for row in probabilities:

            probability = float(
                row[1]
            )

            results.append(

                {

                    "Probability":
                        probability,

                    "ProbabilityPercent":
                        round(
                            probability * 100,
                            2,
                        ),

                    "Risk":
                        BankruptcyPipeline.classify_risk(
                            probability
                        ),

                    "Confidence":
                        round(
                            BankruptcyPipeline.confidence(
                                probability
                            ) * 100,
                            2,
                        ),

                }

            )

        return results