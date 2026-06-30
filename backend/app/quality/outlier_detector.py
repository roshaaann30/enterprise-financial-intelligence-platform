import pandas as pd
from scipy.stats import zscore


class OutlierDetector:

    @staticmethod
    def detect(dataframe: pd.DataFrame):

        outliers = []

        numeric_columns = dataframe.select_dtypes(
            include=["number"]
        ).columns

        for column in numeric_columns:

            scores = zscore(dataframe[column])

            outlier_rows = dataframe[
                abs(scores) > 3
            ]

            if not outlier_rows.empty:

                outliers.append(
                    {
                        "column": column,
                        "count": len(outlier_rows),
                    }
                )

        return {
            "total_outliers": sum(
                row["count"] for row in outliers
            ),
            "outlier_columns": outliers,
        }