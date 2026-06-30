import pandas as pd

from app.risk.models.company_quality_model import (
    CompanyQualityModel,
)

from app.risk.scoring.company_quality_score import (
    CompanyQualityScore,
)


class CompanyQualityPipeline:

    """
    Enterprise Company Quality Pipeline
    """

    ###########################################################
    # Predict
    ###########################################################

    @staticmethod
    def predict(

        financial_health,

        bankruptcy_risk,

        credit_risk,

        investment_score,

    ):

        #######################################################
        # Load Model
        #######################################################

        model = CompanyQualityModel.load()

        #######################################################
        # Build Features
        #######################################################

        features = pd.DataFrame(

            {

                "FinancialHealth":
                    [financial_health],

                "BankruptcyRisk":
                    [bankruptcy_risk],

                "CreditRisk":
                    [credit_risk],

                "InvestmentScore":
                    [investment_score],

            }

        )

        #######################################################
        # Predict Quality Score
        #######################################################

        predicted_score = float(

            model.predict(

                features

            )[0]

        )

        #######################################################
        # Rating
        #######################################################

        rating = (

            CompanyQualityScore.rating(

                predicted_score

            )

        )

        #######################################################
        # Recommendation
        #######################################################

        recommendation = (

            CompanyQualityScore.recommendation(

                predicted_score

            )

        )

        #######################################################
        # Confidence
        #######################################################

        confidence = (

            CompanyQualityScore.confidence(

                predicted_score

            )

        )

        #######################################################
        # Output
        #######################################################

        return {

            "quality_score":

                round(

                    predicted_score,

                    2,

                ),

            "rating":

                rating,

            "recommendation":

                recommendation,

            "confidence":

                confidence,

            "inputs": {

                "financial_health":
                    financial_health,

                "bankruptcy_risk":
                    bankruptcy_risk,

                "credit_risk":
                    credit_risk,

                "investment_score":
                    investment_score,

            },

        }