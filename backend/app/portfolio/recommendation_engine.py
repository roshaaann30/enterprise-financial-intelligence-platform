class RecommendationEngine:

    @staticmethod
    def generate(

        risk_score,

    ):

        if risk_score > 70:

            return (

                "Reduce concentration"

            )

        elif risk_score > 40:

            return (

                "Improve diversification"

            )

        return (

            "Portfolio appears balanced"

        )