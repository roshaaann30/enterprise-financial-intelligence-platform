import pandas as pd


class RollingFeatureGenerator:

    @staticmethod
    def generate(dataframe: pd.DataFrame):

        df = dataframe.copy()

        windows = [5, 10, 20, 50]

        for window in windows:

            # Rolling Mean
            df[f"RollingMean_{window}"] = (
                df["Close"]
                .rolling(window)
                .mean()
            )

            # Rolling Standard Deviation
            df[f"RollingStd_{window}"] = (
                df["Close"]
                .rolling(window)
                .std()
            )

            # Rolling Minimum
            df[f"RollingMin_{window}"] = (
                df["Close"]
                .rolling(window)
                .min()
            )

            # Rolling Maximum
            df[f"RollingMax_{window}"] = (
                df["Close"]
                .rolling(window)
                .max()
            )

            # Rolling Median
            df[f"RollingMedian_{window}"] = (
                df["Close"]
                .rolling(window)
                .median()
            )

            # Rolling Variance
            df[f"RollingVariance_{window}"] = (
                df["Close"]
                .rolling(window)
                .var()
            )

            # Rolling Skewness
            df[f"RollingSkew_{window}"] = (
                df["Close"]
                .rolling(window)
                .skew()
            )

            # Rolling Kurtosis
            df[f"RollingKurtosis_{window}"] = (
                df["Close"]
                .rolling(window)
                .kurt()
            )

            # Rolling Z-Score
            rolling_mean = (
                df["Close"]
                .rolling(window)
                .mean()
            )

            rolling_std = (
                df["Close"]
                .rolling(window)
                .std()
            )

            df[f"RollingZScore_{window}"] = (
                (df["Close"] - rolling_mean)
                / rolling_std
            )

        df = df.bfill()

        return df