import pandas as pd

from app.risk.scoring.company_quality_score import (
    CompanyQualityScore,
)


class QualityDatasetBuilder:

    """
    Enterprise Quality Dataset Builder
    """

    ###########################################################
    # Build Dataset
    ###########################################################

    @staticmethod
    def build(

        dataframe,

    ):

        df = dataframe.copy()

        #######################################################
        # Generate Quality Score
        #######################################################

        quality_scores = []

        ratings = []

        recommendations = []

        for _, row in df.iterrows():

            result = (

                CompanyQualityScore.calculate(

                    financial_health_score=

                    row["FinancialHealth"],

                    bankruptcy_risk=

                    row["BankruptcyRisk"],

                    credit_risk=

                    row["CreditRisk"],

                    investment_score=

                    row["InvestmentScore"],

                )

            )

            quality_scores.append(

                result["quality_score"]

            )

            ratings.append(

                result["rating"]

            )

            recommendations.append(

                result["recommendation"]

            )

        #######################################################
        # Add Targets
        #######################################################

        df["QualityScore"] = quality_scores

        df["QualityRating"] = ratings

        df["Recommendation"] = recommendations

        return df

    ###########################################################
    # Save Dataset
    ###########################################################

    @staticmethod
    def save(

        dataframe,

        path="datasets/risk/company_quality.csv",

    ):

        dataframe.to_csv(

            path,

            index=False,

        )

        return path