import pandas as pd


class ForecastTargetGenerator:

    @staticmethod
    def create_targets(dataframe: pd.DataFrame):

        df = dataframe.copy()

        # Revenue
        if "Revenue" in df.columns:
            df["Target_Revenue"] = (
                df["Revenue"].shift(-1)
            )

        # EPS
        if "EPS" in df.columns:
            df["Target_EPS"] = (
                df["EPS"].shift(-1)
            )

        # Operating Cash Flow
        if "Operating Cash Flow" in df.columns:
            df["Target_OperatingCashFlow"] = (
                df["Operating Cash Flow"].shift(-1)
            )

        # Net Income
        if "Net Income" in df.columns:
            df["Target_NetIncome"] = (
                df["Net Income"].shift(-1)
            )

        return df