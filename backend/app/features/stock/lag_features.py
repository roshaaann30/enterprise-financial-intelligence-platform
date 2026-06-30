import pandas as pd


class LagFeatureGenerator:

    @staticmethod
    def generate(dataframe: pd.DataFrame):

        df = dataframe.copy()

        lag_periods = [
            1,
            2,
            3,
            5,
            10,
            20,
            30,
        ]

        columns = [
            "Open",
            "High",
            "Low",
            "Close",
            "Volume",
        ]

        for column in columns:

            for lag in lag_periods:

                df[f"{column}_Lag_{lag}"] = (
                    df[column].shift(lag)
                )

        # ==========================
        # Returns
        # ==========================

        df["Daily_Return"] = (
            df["Close"].pct_change()
        )

        for lag in lag_periods:

            df[f"Return_Lag_{lag}"] = (
                df["Daily_Return"].shift(lag)
            )

        # ==========================
        # Volume Change
        # ==========================

        df["Volume_Change"] = (
            df["Volume"].pct_change()
        )

        for lag in lag_periods:

            df[f"VolumeChange_Lag_{lag}"] = (
                df["Volume_Change"].shift(lag)
            )

        df = df.bfill()

        return df