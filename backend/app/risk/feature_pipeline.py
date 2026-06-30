import pandas as pd

from app.risk.features.liquidity_features import (
    LiquidityFeatureGenerator,
)

from app.risk.features.profitability_features import (
    ProfitabilityFeatureGenerator,
)

from app.risk.features.leverage_efficiency_features import (
    LeverageEfficiencyFeatureGenerator,
)

from app.risk.features.growth_features import (
    GrowthFeatureGenerator,
)


class RiskFeaturePipeline:

    """
    Enterprise Risk Feature Engineering Pipeline

    Generates all financial risk features used by

    Bankruptcy Prediction

    Credit Risk

    Investment Risk

    Financial Health Score

    Company Quality Score
    """

    @staticmethod
    def process(df):

        ###########################################################
        # Original Dataset
        ###########################################################

        original = df.copy()

        ###########################################################
        # Generate Feature Groups
        ###########################################################

        liquidity = LiquidityFeatureGenerator.generate(
            original
        )

        profitability = ProfitabilityFeatureGenerator.generate(
            original
        )

        leverage = LeverageEfficiencyFeatureGenerator.generate(
            original
        )

        growth = GrowthFeatureGenerator.generate(
            original
        )

        ###########################################################
        # Merge Features
        ###########################################################

        features = pd.concat(

            [

                liquidity,

                profitability,

                leverage,

                growth,

            ],

            axis=1,

        )

        ###########################################################
        # Remove Duplicate Columns
        ###########################################################

        features = features.loc[
            :,
            ~features.columns.duplicated(),
        ]

        ###########################################################
        # Replace Missing Values
        ###########################################################

        features = features.fillna(0)

        ###########################################################
        # Replace Infinite Values
        ###########################################################

        features = features.replace(

            [

                float("inf"),

                float("-inf"),

            ],

            0,

        )

        ###########################################################
        # Feature Summary
        ###########################################################

        summary = {

            "TotalFeatures": len(features.columns),

            "MissingValues": int(
                features.isna().sum().sum()
            ),

            "Samples": len(features),

        }

        ###########################################################
        # Return
        ###########################################################

        return {

            "features": features,

            "summary": summary,

        }