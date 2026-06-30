import pandas as pd


class DatasetMerger:

    @staticmethod
    def merge(
        stock_df: pd.DataFrame,
        financial_df: pd.DataFrame,
        macro_df: pd.DataFrame,
        news_df: pd.DataFrame,
    ):

        dataset = stock_df.copy()

        # Merge Financial Features
        if financial_df is not None:
            dataset = dataset.merge(
                financial_df,
                on="Date",
                how="left",
            )

        # Merge Macro Features
        if macro_df is not None:
            dataset = dataset.merge(
                macro_df,
                on="Date",
                how="left",
            )

        # Merge News Features
        if news_df is not None:
            dataset = dataset.merge(
                news_df,
                on="Date",
                how="left",
            )

        dataset.ffill(inplace=True)
        dataset.bfill(inplace=True)

        return dataset