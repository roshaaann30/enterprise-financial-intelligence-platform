class DiversificationAnalyzer:

    @staticmethod
    def score(

        portfolio_df,

    ):

        holdings = len(

            portfolio_df

        )

        return min(

            holdings * 10,

            100,

        )