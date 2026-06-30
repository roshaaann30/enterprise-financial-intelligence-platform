import pandas as pd

from app.risk.features.financial_ratios import (
    FinancialRatios,
)


class GrowthFeatureGenerator:

    """
    Generates growth and market valuation
    financial features.
    """

    @staticmethod
    def generate(df):

        data = df.copy()

        ###########################################################
        # Validate Required Columns
        ###########################################################

        required_columns = [

            "Revenue",
            "PreviousRevenue",

            "NetIncome",
            "PreviousNetIncome",

            "TotalAssets",
            "PreviousTotalAssets",

            "ShareholderEquity",
            "PreviousShareholderEquity",

            "OperatingCashFlow",
            "CapitalExpenditure",

            "MarketCap",
            "TotalDebt",
            "Cash",
            "EBITDA",

        ]

        missing = [

            col

            for col in required_columns

            if col not in data.columns

        ]

        if missing:

            raise ValueError(

                f"Missing columns: {missing}"

            )

        ###########################################################
        # Revenue Growth
        ###########################################################

        data["RevenueGrowth"] = data.apply(

            lambda row: FinancialRatios.growth_rate(

                row["Revenue"],

                row["PreviousRevenue"],

            ),

            axis=1,

        )

        ###########################################################
        # Net Income Growth
        ###########################################################

        data["NetIncomeGrowth"] = data.apply(

            lambda row: FinancialRatios.growth_rate(

                row["NetIncome"],

                row["PreviousNetIncome"],

            ),

            axis=1,

        )

        ###########################################################
        # Asset Growth
        ###########################################################

        data["AssetGrowth"] = data.apply(

            lambda row: FinancialRatios.growth_rate(

                row["TotalAssets"],

                row["PreviousTotalAssets"],

            ),

            axis=1,

        )

        ###########################################################
        # Equity Growth
        ###########################################################

        data["EquityGrowth"] = data.apply(

            lambda row: FinancialRatios.growth_rate(

                row["ShareholderEquity"],

                row["PreviousShareholderEquity"],

            ),

            axis=1,

        )

        ###########################################################
        # Free Cash Flow
        ###########################################################

        data["FreeCashFlow"] = data.apply(

            lambda row: FinancialRatios.free_cash_flow(

                row["OperatingCashFlow"],

                row["CapitalExpenditure"],

            ),

            axis=1,

        )

        ###########################################################
        # Enterprise Value
        ###########################################################

        data["EnterpriseValue"] = data.apply(

            lambda row: FinancialRatios.enterprise_value(

                row["MarketCap"],

                row["TotalDebt"],

                row["Cash"],

            ),

            axis=1,

        )

        ###########################################################
        # EV / EBITDA
        ###########################################################

        data["EVtoEBITDA"] = data.apply(

            lambda row: FinancialRatios.ev_to_ebitda(

                FinancialRatios.enterprise_value(

                    row["MarketCap"],

                    row["TotalDebt"],

                    row["Cash"],

                ),

                row["EBITDA"],

            ),

            axis=1,

        )

        ###########################################################
        # Return Features
        ###########################################################

        return data[

            [

                "RevenueGrowth",

                "NetIncomeGrowth",

                "AssetGrowth",

                "EquityGrowth",

                "FreeCashFlow",

                "EnterpriseValue",

                "EVtoEBITDA",

            ]

        ]