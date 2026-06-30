import pandas as pd


class InvalidValueDetector:

    @staticmethod
    def detect(dataframe: pd.DataFrame):

        invalid_rows = []

        numeric_columns = dataframe.select_dtypes(
            include=["number"]
        ).columns

        for column in numeric_columns:

            invalid = dataframe[dataframe[column] < 0]

            if not invalid.empty:

                invalid_rows.append(
                    {
                        "column": column,
                        "count": len(invalid),
                    }
                )

        return {
            "total_invalid": sum(
                row["count"] for row in invalid_rows
            ),
            "invalid_columns": invalid_rows,
        }