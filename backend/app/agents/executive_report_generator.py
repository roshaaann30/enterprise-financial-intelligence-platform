class ExecutiveReportGenerator:

    """
    Enterprise Executive Report
    """

    @staticmethod
    def generate(

        results,

    ):

        financial = (

            results

            .get(

                "FinancialAnalystAgent",

                {}

            )

            .get(

                "financial_analysis",

                {}

            )

        )

        news = (

            results

            .get(

                "NewsAnalystAgent",

                {}

            )

            .get(

                "news_analysis",

                {}

            )

        )

        risk = (

            results

            .get(

                "RiskAnalystAgent",

                {}

            )

            .get(

                "risk_analysis",

                {}

            )

        )

        forecast = (

            results

            .get(

                "ForecastingAgent",

                {}

            )

            .get(

                "forecasting_analysis",

                {}

            )

        )

        portfolio = (

            results

            .get(

                "PortfolioAnalystAgent",

                {}

            )

            .get(

                "portfolio_analysis",

                {}

            )

        )

        return {

            "financial_health":

                financial.get(

                    "financial_health"

                ),

            "investment_strength_score":

                financial.get(

                    "investment_strength_score"

                ),

            "market_sentiment":

                news.get(

                    "market_sentiment"

                ),

            "enterprise_risk_score":

                risk.get(

                    "enterprise_risk_score"

                ),

            "forecast_outlook":

                forecast.get(

                    "forecast_outlook"

                ),

            "investment_rating":

                portfolio.get(

                    "investment_rating"

                ),

            "recommendation":

                portfolio.get(

                    "recommendation"

                ),

        }