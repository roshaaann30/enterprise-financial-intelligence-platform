import numpy as np


class FinancialHealthScore:

    """
    Enterprise Financial Health Score Engine

    Computes an overall financial health score
    between 0 and 100.
    """

    ##########################################################
    # Constructor
    ##########################################################

    def __init__(

        self,

        liquidity_weight=0.20,

        profitability_weight=0.25,

        leverage_weight=0.20,

        growth_weight=0.20,

        efficiency_weight=0.15,

    ):

        self.weights = {

            "Liquidity": liquidity_weight,

            "Profitability": profitability_weight,

            "Leverage": leverage_weight,

            "Growth": growth_weight,

            "Efficiency": efficiency_weight,

        }

    ##########################################################
    # Clamp Score
    ##########################################################

    @staticmethod
    def clamp(score):

        return max(

            0,

            min(

                100,

                float(score),

            ),

        )

    ##########################################################
    # Weighted Health Score
    ##########################################################

    def calculate(

        self,

        liquidity,

        profitability,

        leverage,

        growth,

        efficiency,

    ):

        weighted_score = (

            liquidity * self.weights["Liquidity"]

            + profitability * self.weights["Profitability"]

            + leverage * self.weights["Leverage"]

            + growth * self.weights["Growth"]

            + efficiency * self.weights["Efficiency"]

        )

        return self.clamp(

            weighted_score

        )

    ##########################################################
    # Batch Calculation
    ##########################################################

    def calculate_dataframe(

        self,

        dataframe,

    ):

        required_columns = [

            "LiquidityScore",

            "ProfitabilityScore",

            "LeverageScore",

            "GrowthScore",

            "EfficiencyScore",

        ]

        missing = [

            column

            for column in required_columns

            if column not in dataframe.columns

        ]

        if missing:

            raise ValueError(

                f"Missing columns: {missing}"

            )

        df = dataframe.copy()

        df["FinancialHealthScore"] = df.apply(

            lambda row: self.calculate(

                liquidity=row["LiquidityScore"],

                profitability=row["ProfitabilityScore"],

                leverage=row["LeverageScore"],

                growth=row["GrowthScore"],

                efficiency=row["EfficiencyScore"],

            ),

            axis=1,

        )

        return df

    ##########################################################
    # Statistics
    ##########################################################

    @staticmethod
    def summary(scores):

        scores = np.asarray(scores)

        return {

            "Mean": float(scores.mean()),

            "Median": float(np.median(scores)),

            "Minimum": float(scores.min()),

            "Maximum": float(scores.max()),

            "StandardDeviation": float(scores.std()),

        }