class PortfolioRiskEngine:

    @staticmethod
    def score(

        concentration,

        diversification,

        correlation,

    ):

        risk = (

            concentration

            * 0.5

            +

            (100 - diversification)

            * 0.3

            +

            correlation

            * 100

            * 0.2

        )

        return round(

            risk,

            2,

        )