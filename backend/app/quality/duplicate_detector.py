import pandas as pd


class DuplicateDetector:

    @staticmethod
    def detect(dataframe: pd.DataFrame):

        duplicates = dataframe.duplicated()

        duplicate_rows = dataframe[duplicates]

        return {
            "total_duplicates": int(duplicates.sum()),
            "duplicate_rows": duplicate_rows,
        }