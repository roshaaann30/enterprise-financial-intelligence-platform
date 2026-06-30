import pandas as pd


class GrowthFeatureGenerator:

    @staticmethod
    def generate(dataframe: pd.DataFrame):

        df = dataframe.copy()

        # Revenue Growth
        df["Revenue_Growth"] = (
            df["Revenue"].pct_change()
        )

        # Gross Profit Growth
        df["Gross_Profit_Growth"] = (
            df["Gross Profit"].pct_change()
        )

        # Operating Income Growth
        df["Operating_Income_Growth"] = (
            df["Operating Income"].pct_change()
        )

        # Net Income Growth
        df["Net_Income_Growth"] = (
            df["Net Income"].pct_change()
        )

        # EPS Growth
        df["EPS_Growth"] = (
            df["EPS"].pct_change()
        )

        # Assets Growth
        df["Assets_Growth"] = (
            df["Total Assets"].pct_change()
        )

        # Equity Growth
        df["Equity_Growth"] = (
            df["Total Equity"].pct_change()
        )

        # Debt Growth
        df["Debt_Growth"] = (
            df["Total Debt"].pct_change()
        )

        # Cash Growth
        df["Cash_Growth"] = (
            df["Cash"].pct_change()
        )

        # Operating Cash Flow Growth
        df["Operating_CF_Growth"] = (
            df["Operating Cash Flow"].pct_change()
        )

        df.fillna(0, inplace=True)

        return df