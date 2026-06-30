from app.risk.models.investment_risk_model import (
    InvestmentRiskModel,
)

from app.risk.models.return_prediction_model import (
    ReturnPredictionModel,
)

from app.risk.preprocessing.investment_preprocessor import (
    InvestmentPreprocessor,
)

from app.risk.features.investment_features import (
    InvestmentFeatures,
)


class InvestmentPipeline:

    """
    Enterprise Investment Pipeline
    """

    ###########################################################
    # Investment Score
    ###########################################################

    @staticmethod
    def calculate_investment_score(

        risk_probability,

        expected_return,

    ):

        risk_score = (

            100

            - (risk_probability * 100)

        )

        return_score = min(

            100,

            max(

                0,

                expected_return * 2,

            ),

        )

        score = (

            risk_score * 0.6

            +

            return_score * 0.4

        )

        return round(

            score,

            2,

        )

    ###########################################################
    # Recommendation
    ###########################################################

    @staticmethod
    def recommendation(

        investment_score,

    ):

        if investment_score >= 80:

            return "BUY"

        elif investment_score >= 60:

            return "HOLD"

        else:

            return "SELL"

    ###########################################################
    # Risk Category
    ###########################################################

    @staticmethod
    def risk_category(

        risk_probability,

    ):

        risk = risk_probability * 100

        if risk < 20:

            return "Very Low"

        elif risk < 40:

            return "Low"

        elif risk < 60:

            return "Moderate"

        elif risk < 80:

            return "High"

        else:

            return "Very High"

    ###########################################################
    # Confidence
    ###########################################################

    @staticmethod
    def confidence(

        probability,

    ):

        return round(

            min(

                1.0,

                abs(
                    probability - 0.5
                ) * 2,

            ) * 100,

            2,

        )

    ###########################################################
    # Predict
    ###########################################################

    @staticmethod
    def predict(

        raw_features,

    ):

        #######################################################
        # Generate Features
        #######################################################

        features = (

            InvestmentFeatures.generate(

                raw_features

            )

        )

        #######################################################
        # Scale
        #######################################################

        scaler = (

            InvestmentPreprocessor.load_scaler()

        )

        scaled = scaler.transform(

            features

        )

        #######################################################
        # Load Models
        #######################################################

        risk_model = (

            InvestmentRiskModel.load()

        )

        return_model = (

            ReturnPredictionModel.load()

        )

        #######################################################
        # Predictions
        #######################################################

        risk_probability = float(
            risk_model.predict_proba(
                scaled
                )[0][1]
                )

        expected_return = float(

            return_model.predict(

                scaled

            )[0]

        )

        #######################################################
        # Investment Score
        #######################################################

        investment_score = (

            InvestmentPipeline.calculate_investment_score(

                risk_probability,

                expected_return,

            )

        )

        #######################################################
        # Output
        #######################################################

        return {

            "risk_probability":

                round(

                    risk_probability,

                    4,

                ),

            "risk_percentage":

                round(

                    risk_probability * 100,

                    2,

                ),

            "expected_return":

                round(

                    expected_return,

                    2,

                ),

            "investment_score":

                investment_score,

            "risk_category":

                InvestmentPipeline.risk_category(

                    risk_probability

                ),

            "recommendation":

                InvestmentPipeline.recommendation(

                    investment_score

                ),

            "confidence":

                InvestmentPipeline.confidence(

                    risk_probability

                ),

        }