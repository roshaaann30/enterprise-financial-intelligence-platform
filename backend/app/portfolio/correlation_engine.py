import numpy as np


class CorrelationEngine:

    @staticmethod
    def estimate(

        portfolio_df,

    ):

        holdings = len(

            portfolio_df

        )

        return round(

            max(

                0.1,

                1

                /

                holdings

            ),

            2,

        )