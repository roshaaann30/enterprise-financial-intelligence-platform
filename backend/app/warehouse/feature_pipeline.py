import pandas as pd


class FeaturePipeline:

    @staticmethod
    def generate_features(dataframe: pd.DataFrame):

        dataframe = dataframe.copy()

        dataframe["Daily_Return"] = (
            dataframe["Close"].pct_change()
        )

        dataframe["MA_5"] = (
            dataframe["Close"].rolling(5).mean()
        )

        dataframe["MA_20"] = (
            dataframe["Close"].rolling(20).mean()
        )

        dataframe["Volatility"] = (
            dataframe["Daily_Return"]
            .rolling(20)
            .std()
        )

        dataframe.dropna(inplace=True)

        return dataframe