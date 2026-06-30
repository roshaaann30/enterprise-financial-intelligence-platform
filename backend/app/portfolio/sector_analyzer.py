class SectorAnalyzer:

    @staticmethod
    def analyze(

        portfolio_df,

    ):

        sector_weights = (

            portfolio_df

            .groupby(

                "sector"

            )["weight"]

            .sum()

            .to_dict()

        )

        return sector_weights