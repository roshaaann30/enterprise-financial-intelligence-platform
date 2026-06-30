import pandas as pd

from app.risk.features.financial_ratios import (
    FinancialRatios,
)


class ProfitabilityFeatureGenerator:

    """
    Generates profitability-related financial features.
    """

    @staticmethod
    def generate(df):

        data = df.copy()

        ###########################################################
        # Gross Margin
        ###########################################################

        data["GrossMargin"] = data.apply(

            lambda row: FinancialRatios.gross_margin(

                row["Revenue"],

                row["CostOfRevenue"],

            ),

            axis=1,

        )

        ###########################################################
        # Operating Margin
        ###########################################################

        data["OperatingMargin"] = data.apply(

            lambda row: FinancialRatios.operating_margin(

                row["OperatingIncome"],

                row["Revenue"],

            ),

            axis=1,

        )

        ###########################################################
        # Net Margin
        ###########################################################

        data["NetMargin"] = data.apply(

            lambda row: FinancialRatios.net_margin(

                row["NetIncome"],

                row["Revenue"],

            ),

            axis=1,

        )

        ###########################################################
        # Return On Assets
        ###########################################################

        data["ROA"] = data.apply(

            lambda row: FinancialRatios.roa(

                row["NetIncome"],

                row["TotalAssets"],

            ),

            axis=1,

        )

        ###########################################################
        # Return On Equity
        ###########################################################

        data["ROE"] = data.apply(

            lambda row: FinancialRatios.roe(

                row["NetIncome"],

                row["ShareholderEquity"],

            ),

            axis=1,

        )

        ###########################################################
        # Return On Invested Capital
        ###########################################################

        data["ROIC"] = data.apply(

            lambda row: FinancialRatios.roic(

                row["OperatingIncome"],

                row["InvestedCapital"],

            ),

            axis=1,

        )

        ###########################################################
        # Return Only Profitability Features
        ###########################################################

        return data[
            [
                "GrossMargin",
                "OperatingMargin",
                "NetMargin",
                "ROA",
                "ROE",
                "ROIC",
            ]
        ]