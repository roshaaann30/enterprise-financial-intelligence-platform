import pandas as pd

from app.risk.features.financial_ratios import (
    FinancialRatios,
)


class LeverageEfficiencyFeatureGenerator:

    """
    Generates leverage and efficiency related
    financial features.
    """

    @staticmethod
    def generate(df):

        data = df.copy()

        ###########################################################
        # Validate Required Columns
        ###########################################################

        required_columns = [

            "TotalDebt",

            "ShareholderEquity",

            "TotalAssets",

            "EBIT",

            "InterestExpense",

            "Revenue",

            "Inventory",

            "AccountsReceivable",

            "CostOfRevenue",

        ]

        missing = [

            column

            for column in required_columns

            if column not in data.columns

        ]

        if missing:

            raise ValueError(

                f"Missing columns: {missing}"

            )

        ###########################################################
        # Debt Ratio
        ###########################################################

        data["DebtRatio"] = data.apply(

            lambda row: FinancialRatios.debt_ratio(

                row["TotalDebt"],

                row["TotalAssets"],

            ),

            axis=1,

        )

        ###########################################################
        # Debt To Equity
        ###########################################################

        data["DebtToEquity"] = data.apply(

            lambda row: FinancialRatios.debt_to_equity(

                row["TotalDebt"],

                row["ShareholderEquity"],

            ),

            axis=1,

        )

        ###########################################################
        # Equity Ratio
        ###########################################################

        data["EquityRatio"] = data.apply(

            lambda row: FinancialRatios.equity_ratio(

                row["ShareholderEquity"],

                row["TotalAssets"],

            ),

            axis=1,

        )

        ###########################################################
        # Interest Coverage
        ###########################################################

        data["InterestCoverage"] = data.apply(

            lambda row: FinancialRatios.interest_coverage(

                row["EBIT"],

                row["InterestExpense"],

            ),

            axis=1,

        )

        ###########################################################
        # Asset Turnover
        ###########################################################

        data["AssetTurnover"] = data.apply(

            lambda row: FinancialRatios.asset_turnover(

                row["Revenue"],

                row["TotalAssets"],

            ),

            axis=1,

        )

        ###########################################################
        # Inventory Turnover
        ###########################################################

        data["InventoryTurnover"] = data.apply(

            lambda row: FinancialRatios.inventory_turnover(

                row["CostOfRevenue"],

                row["Inventory"],

            ),

            axis=1,

        )

        ###########################################################
        # Receivable Turnover
        ###########################################################

        data["ReceivableTurnover"] = data.apply(

            lambda row: FinancialRatios.receivable_turnover(

                row["Revenue"],

                row["AccountsReceivable"],

            ),

            axis=1,

        )

        ###########################################################
        # Return Features
        ###########################################################

        return data[

            [

                "DebtRatio",

                "DebtToEquity",

                "EquityRatio",

                "InterestCoverage",

                "AssetTurnover",

                "InventoryTurnover",

                "ReceivableTurnover",

            ]

        ]