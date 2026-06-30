from pathlib import Path

import pandas as pd


class InvestmentDataset:

    """
    Enterprise Investment Dataset Loader
    """

    ###########################################################
    # Constructor
    ###########################################################

    def __init__(

        self,

        dataset_path=None,

    ):

        if dataset_path is None:

            dataset_path = (

                Path(__file__)
                .resolve()
                .parents[3]

                / "datasets"

                / "risk"

                / "investment.csv"

            )

        self.dataset_path = Path(
            dataset_path
        )

    ###########################################################
    # Load Dataset
    ###########################################################

    def load(self):

        if not self.dataset_path.exists():

            raise FileNotFoundError(

                f"Dataset not found:\n"
                f"{self.dataset_path}"

            )

        return pd.read_csv(
            self.dataset_path
        )

    ###########################################################
    # Validate Dataset
    ###########################################################

    def validate(

        self,

        df,

    ):

        required_columns = [

            "NetIncome",
            "ShareholderEquity",
            "TotalAssets",
            "TotalLiabilities",
            "CurrentAssets",
            "CurrentLiabilities",
            "Inventory",
            "Revenue",
            "PreviousRevenue",
            "OperatingIncome",
            "PreviousNetIncome",
            "OperatingCashFlow",
            "EBIT",
            "InterestExpense",
            "InvestmentRisk",

        ]

        missing = [

            col

            for col in required_columns

            if col not in df.columns

        ]

        if missing:

            raise ValueError(

                f"Missing columns: {missing}"

            )

        return True

    ###########################################################
    # Clean
    ###########################################################

    def clean(

        self,

        df,

    ):

        df = df.copy()

        df = df.drop_duplicates()

        numeric_columns = (

            df.select_dtypes(
                include="number"
            )
            .columns
        )

        df[numeric_columns] = (

            df[numeric_columns]

            .fillna(

                df[
                    numeric_columns
                ].median()

            )

        )

        return df

    ###########################################################
    # Split
    ###########################################################

    def split(

        self,

        df,

        target_column="InvestmentRisk",

    ):

        X = df.drop(
            columns=[target_column]
        )

        y = df[target_column]

        return X, y

    ###########################################################
    # Process
    ###########################################################

    def process(

        self,

        target_column="InvestmentRisk",

    ):

        df = self.load()

        self.validate(
            df
        )

        df = self.clean(
            df
        )

        X, y = self.split(
            df,
            target_column,
        )

        return {

            "data": df,

            "X": X,

            "y": y,

        }