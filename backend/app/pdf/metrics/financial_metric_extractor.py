import re


class FinancialMetricExtractor:

    """
    Extract financial metrics from tables/text
    """

    METRICS = [

        "Revenue",

        "Net Income",

        "EPS",

        "EBITDA",

        "Operating Income",

        "Cash",

        "Debt",

        "Free Cash Flow",

        "Total Assets",

        "Total Liabilities",

    ]

    @staticmethod
    def extract_from_tables(

        tables,

    ):

        results = {}

        for table in tables:

            df = table["data"]

            for _, row in df.iterrows():

                row_text = " ".join(

                    str(x)

                    for x in row

                )

                for metric in (

                    FinancialMetricExtractor.METRICS

                ):

                    if metric.lower() in row_text.lower():

                        results[metric] = row.tolist()

        return results