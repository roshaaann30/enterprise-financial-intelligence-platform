import numpy as np


class CategoryScores:

    """
    Enterprise Financial Category Scoring

    Converts financial ratios into
    standardized scores (0-100).
    """

    ##############################################################
    # Clamp
    ##############################################################

    @staticmethod
    def clamp(value):

        return max(
            0.0,
            min(
                100.0,
                float(value),
            ),
        )

    ##############################################################
    # Linear Score
    ##############################################################

    @staticmethod
    def linear_score(

        value,

        minimum,

        maximum,

        reverse=False,

    ):

        if maximum == minimum:

            return 50.0

        score = (

            (value - minimum)

            /

            (maximum - minimum)

        ) * 100

        if reverse:

            score = 100 - score

        return CategoryScores.clamp(score)

    ##############################################################
    # Liquidity
    ##############################################################

    @staticmethod
    def liquidity_score(features):

        scores = [

            CategoryScores.linear_score(

                features["CurrentRatio"],

                0,

                3,

            ),

            CategoryScores.linear_score(

                features["QuickRatio"],

                0,

                3,

            ),

            CategoryScores.linear_score(

                features["CashRatio"],

                0,

                2,

            ),

            CategoryScores.linear_score(

                features["OperatingCashFlowRatio"],

                0,

                2,

            ),

        ]

        return float(np.mean(scores))

    ##############################################################
    # Profitability
    ##############################################################

    @staticmethod
    def profitability_score(features):

        scores = [

            CategoryScores.linear_score(

                features["GrossMargin"],

                0,

                0.7,

            ),

            CategoryScores.linear_score(

                features["OperatingMargin"],

                0,

                0.4,

            ),

            CategoryScores.linear_score(

                features["NetMargin"],

                0,

                0.3,

            ),

            CategoryScores.linear_score(

                features["ROA"],

                0,

                0.25,

            ),

            CategoryScores.linear_score(

                features["ROE"],

                0,

                0.40,

            ),

            CategoryScores.linear_score(

                features["ROIC"],

                0,

                0.35,

            ),

        ]

        return float(np.mean(scores))

    ##############################################################
    # Leverage
    ##############################################################

    @staticmethod
    def leverage_score(features):

        scores = [

            CategoryScores.linear_score(

                features["DebtRatio"],

                0,

                1,

                reverse=True,

            ),

            CategoryScores.linear_score(

                features["DebtToEquity"],

                0,

                3,

                reverse=True,

            ),

            CategoryScores.linear_score(

                features["EquityRatio"],

                0,

                1,

            ),

            CategoryScores.linear_score(

                features["InterestCoverage"],

                0,

                15,

            ),

        ]

        return float(np.mean(scores))

    ##############################################################
    # Growth
    ##############################################################

    @staticmethod
    def growth_score(features):

        scores = [

            CategoryScores.linear_score(

                features["RevenueGrowth"],

                -0.2,

                0.4,

            ),

            CategoryScores.linear_score(

                features["NetIncomeGrowth"],

                -0.3,

                0.5,

            ),

            CategoryScores.linear_score(

                features["AssetGrowth"],

                -0.2,

                0.4,

            ),

            CategoryScores.linear_score(

                features["EquityGrowth"],

                -0.2,

                0.4,

            ),

        ]

        return float(np.mean(scores))

    ##############################################################
    # Efficiency
    ##############################################################

    @staticmethod
    def efficiency_score(features):

        scores = [

            CategoryScores.linear_score(

                features["AssetTurnover"],

                0,

                2,

            ),

            CategoryScores.linear_score(

                features["InventoryTurnover"],

                0,

                15,

            ),

            CategoryScores.linear_score(

                features["ReceivableTurnover"],

                0,

                20,

            ),

        ]

        return float(np.mean(scores))

    ##############################################################
    # Overall Categories
    ##############################################################

    @staticmethod
    def calculate(features):

        return {

            "LiquidityScore":

                CategoryScores.liquidity_score(
                    features
                ),

            "ProfitabilityScore":

                CategoryScores.profitability_score(
                    features
                ),

            "LeverageScore":

                CategoryScores.leverage_score(
                    features
                ),

            "GrowthScore":

                CategoryScores.growth_score(
                    features
                ),

            "EfficiencyScore":

                CategoryScores.efficiency_score(
                    features
                ),

        }