import pandas as pd

from app.risk.features.financial_ratios import (
    FinancialRatios,
)


class LiquidityFeatureGenerator:

    """
    Generates liquidity-related financial features.
    """

    @staticmethod
    def generate(df):

        data = df.copy()

        ###########################################################
        # Current Ratio
        ###########################################################

        data["CurrentRatio"] = data.apply(

            lambda row: FinancialRatios.current_ratio(

                row["CurrentAssets"],

                row["CurrentLiabilities"],

            ),

            axis=1,

        )

        ###########################################################
        # Quick Ratio
        ###########################################################

        data["QuickRatio"] = data.apply(

            lambda row: FinancialRatios.quick_ratio(

                row["CurrentAssets"],

                row["Inventory"],

                row["CurrentLiabilities"],

            ),

            axis=1,

        )

        ###########################################################
        # Cash Ratio
        ###########################################################

        data["CashRatio"] = data.apply(

            lambda row: FinancialRatios.cash_ratio(

                row["Cash"],

                row["CurrentLiabilities"],

            ),

            axis=1,

        )

        ###########################################################
        # Working Capital
        ###########################################################

        data["WorkingCapital"] = data.apply(

            lambda row: FinancialRatios.working_capital(

                row["CurrentAssets"],

                row["CurrentLiabilities"],

            ),

            axis=1,

        )

        ###########################################################
        # Operating Cash Flow Ratio
        ###########################################################

        data["OperatingCashFlowRatio"] = data.apply(

            lambda row: FinancialRatios.operating_cashflow_ratio(

                row["OperatingCashFlow"],

                row["CurrentLiabilities"],

            ),

            axis=1,

        )

        ###########################################################
        # Return Only New Features
        ###########################################################

        return data[
            [
                "CurrentRatio",
                "QuickRatio",
                "CashRatio",
                "WorkingCapital",
                "OperatingCashFlowRatio",
            ]
        ]