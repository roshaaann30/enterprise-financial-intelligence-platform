import pandas as pd


class MissingValueDetector:

    @staticmethod
    def detect(dataframe: pd.DataFrame):

        missing = dataframe.isnull().sum()

        total_missing = int(missing.sum())

        return {
            "total_missing": total_missing,
            "missing_columns": missing[missing > 0].to_dict(),
        }