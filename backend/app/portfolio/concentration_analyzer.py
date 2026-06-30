class ConcentrationAnalyzer:

    @staticmethod
    def score(

        portfolio_df,

    ):

        max_weight = (

            portfolio_df["weight"]

            .max()

        )

        return round(

            max_weight,

            2,

        )