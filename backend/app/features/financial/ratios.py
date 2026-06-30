import pandas as pd


class FinancialFeatureGenerator:

    @staticmethod
    def generate(dataframe: pd.DataFrame):

        df = dataframe.copy()

        # Profitability
        df["Gross_Margin"] = (
            df["Gross Profit"] / df["Revenue"]
        )

        df["Operating_Margin"] = (
            df["Operating Income"] / df["Revenue"]
        )

        df["Net_Margin"] = (
            df["Net Income"] / df["Revenue"]
        )

        # Liquidity
        df["Current_Ratio"] = (
            df["Current Assets"]
            / df["Current Liabilities"]
        )

        df["Quick_Ratio"] = (
            (
                df["Current Assets"]
                - df["Inventory"]
            )
            / df["Current Liabilities"]
        )

        # Leverage
        df["Debt_to_Equity"] = (
            df["Total Debt"]
            / df["Total Equity"]
        )

        df["Debt_Ratio"] = (
            df["Total Debt"]
            / df["Total Assets"]
        )

        # Efficiency
        df["Asset_Turnover"] = (
            df["Revenue"]
            / df["Total Assets"]
        )

        df["Inventory_Turnover"] = (
            df["Cost Of Revenue"]
            / df["Inventory"]
        )

        # Returns
        df["ROA"] = (
            df["Net Income"]
            / df["Total Assets"]
        )

        df["ROE"] = (
            df["Net Income"]
            / df["Total Equity"]
        )

        df["ROIC"] = (
            df["Operating Income"]
            / (
                df["Total Debt"]
                + df["Total Equity"]
            )
        )

        return df