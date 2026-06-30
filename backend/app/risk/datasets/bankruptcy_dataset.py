from pathlib import Path

import pandas as pd


class BankruptcyDataset:

    """
    Enterprise Bankruptcy Dataset Loader

    Loads and validates bankruptcy datasets.
    """

    ###############################################################
    # Constructor
    ###############################################################

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

                / "bankruptcy.csv"

            )

        self.dataset_path = Path(dataset_path)

    ###############################################################
    # Load Dataset
    ###############################################################

    def load(self):

        if not self.dataset_path.exists():

            raise FileNotFoundError(

                f"Dataset not found:\n{self.dataset_path}"

            )

        df = pd.read_csv(

            self.dataset_path

        )

        return df

    ###############################################################
    # Validate Dataset
    ###############################################################

    def validate(

        self,

        df,

        target_column="Bankrupt",

    ):

        if target_column not in df.columns:

            raise ValueError(

                f"Target column '{target_column}' not found."

            )

        if df.empty:

            raise ValueError(

                "Dataset is empty."

            )

        return True

    ###############################################################
    # Clean Dataset
    ###############################################################

    def clean(

        self,

        df,

    ):

        df = df.copy()

        ###########################################################

        df = df.drop_duplicates()

        ###########################################################

        numeric_columns = df.select_dtypes(

            include="number"

        ).columns

        df[numeric_columns] = df[

            numeric_columns

        ].fillna(

            df[numeric_columns].median()

        )

        ###########################################################

        categorical_columns = df.select_dtypes(

            exclude="number"

        ).columns

        for column in categorical_columns:

            df[column] = df[column].fillna(

                df[column].mode()[0]

            )

        return df

    ###############################################################
    # Split
    ###############################################################

    def split(

        self,

        df,

        target_column="Bankrupt",

    ):

        X = df.drop(

            columns=[target_column]

        )

        y = df[target_column]

        return X, y

    ###############################################################
    # Complete Pipeline
    ###############################################################

    def process(
    self,
    target_column="Bankrupt?",
    ):

        df = self.load()

        self.validate(

            df,

            target_column,

        )

        df = self.clean(

            df,

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