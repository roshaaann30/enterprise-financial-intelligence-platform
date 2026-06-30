from app.risk.models.credit_risk_model import (
    CreditRiskModel,
)

from app.risk.preprocessing.credit_preprocessor import (
    CreditPreprocessor,
)


class CreditPipeline:

    """
    Enterprise Credit Risk Prediction Pipeline
    """

    ###########################################################
    # Credit Score
    ###########################################################

    @staticmethod
    def calculate_credit_score(
        default_probability,
    ):

        score = int(

            850

            -

            (default_probability * 550)

        )

        score = max(

            300,

            min(

                score,

                850,

            ),

        )

        return score

    ###########################################################
    # Risk Category
    ###########################################################

    @staticmethod
    def classify_credit(
        score,
    ):

        if score >= 800:

            return "Excellent"

        elif score >= 740:

            return "Very Good"

        elif score >= 670:

            return "Good"

        elif score >= 580:

            return "Fair"

        else:

            return "Poor"

    ###########################################################
    # Confidence
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
    # Predict
    ###########################################################

    @staticmethod
    def predict(
        features,
        model_path="credit_risk_model.pkl",
    ):

        #######################################################
        # Load Model
        #######################################################

        model = CreditRiskModel.load(
            model_path
        )

        #######################################################
        # Load Scaler
        #######################################################

        scaler = CreditPreprocessor.load_scaler()

        #######################################################
        # Scale Features
        #######################################################

        scaled_features = scaler.transform(
            features
        )

        #######################################################
        # Probability
        #######################################################

        probability = float(

            model.predict_proba(
                scaled_features
            )[0][1]

        )

        #######################################################
        # Credit Score
        #######################################################

        credit_score = (

            CreditPipeline.calculate_credit_score(

                probability

            )

        )

        #######################################################
        # Category
        #######################################################

        risk_category = (

            CreditPipeline.classify_credit(

                credit_score

            )

        )

        #######################################################
        # Confidence
        #######################################################

        confidence = (

            CreditPipeline.confidence(

                probability

            )

        )

        #######################################################
        # Return
        #######################################################

        return {

            "default_probability":
                probability,

            "default_percentage":
                round(
                    probability * 100,
                    2,
                ),

            "credit_score":
                credit_score,

            "risk_category":
                risk_category,

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
        model_path="credit_risk_model.pkl",
    ):

        model = CreditRiskModel.load(
            model_path
        )

        scaler = CreditPreprocessor.load_scaler()

        scaled = scaler.transform(
            dataframe
        )

        probabilities = model.predict_proba(
            scaled
        )

        results = []

        for row in probabilities:

            probability = float(
                row[1]
            )

            credit_score = (

                CreditPipeline.calculate_credit_score(
                    probability
                )

            )

            results.append(

                {

                    "DefaultProbability":
                        probability,

                    "CreditScore":
                        credit_score,

                    "RiskCategory":

                        CreditPipeline.classify_credit(
                            credit_score
                        ),

                    "Confidence":

                        round(

                            CreditPipeline.confidence(
                                probability
                            ) * 100,

                            2,

                        ),

                }

            )

        return results