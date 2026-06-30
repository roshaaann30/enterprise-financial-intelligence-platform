from app.agents.base_agent import (
    BaseAgent,
)


class ForecastingAgent(

    BaseAgent

):

    """
    Enterprise Forecasting Agent
    """

    ###########################################################
    # Constructor
    ###########################################################

    def __init__(

        self,

    ):

        super().__init__(

            "ForecastingAgent"

        )

    ###########################################################
    # Revenue Forecast
    ###########################################################

    @staticmethod
    def revenue_forecast(

        financial_score,

        news_score,

        risk_score,

    ):

        growth = 10

        growth += (

            financial_score - 50

        ) * 0.20

        growth += (

            news_score - 50

        ) * 0.10

        growth -= (

            risk_score - 50

        ) * 0.15

        return round(

            growth,

            2,

        )

    ###########################################################
    # EPS Forecast
    ###########################################################

    @staticmethod
    def eps_forecast(

        revenue_growth,

    ):

        return round(

            revenue_growth * 0.80,

            2,

        )

    ###########################################################
    # Cash Flow Forecast
    ###########################################################

    @staticmethod
    def cash_flow_forecast(

        revenue_growth,

    ):

        return round(

            revenue_growth * 0.70,

            2,

        )

    ###########################################################
    # Margin Forecast
    ###########################################################

    @staticmethod
    def margin_forecast(

        revenue_growth,

    ):

        return round(

            revenue_growth * 0.45,

            2,

        )

    ###########################################################
    # Confidence
    ###########################################################

    @staticmethod
    def confidence(

        financial_score,

        news_score,

        risk_score,

    ):

        confidence = (

            financial_score * 0.40

            +

            news_score * 0.30

            +

            (100 - risk_score) * 0.30

        )

        return round(

            confidence,

            2,

        )

    ###########################################################
    # Scenario Analysis
    ###########################################################

    @staticmethod
    def scenarios(

        revenue_growth,

    ):

        return {

            "bull_case":

                round(

                    revenue_growth * 1.30,

                    2,

                ),

            "base_case":

                revenue_growth,

            "bear_case":

                round(

                    revenue_growth * 0.70,

                    2,

                ),

        }

    ###########################################################
    # Outlook
    ###########################################################

    @staticmethod
    def outlook(

        revenue_growth,

    ):

        if revenue_growth >= 20:

            return "Very Positive"

        elif revenue_growth >= 12:

            return "Positive"

        elif revenue_growth >= 5:

            return "Neutral"

        return "Negative"

    ###########################################################
    # Recommendation
    ###########################################################

    @staticmethod
    def recommendation(

        outlook,

    ):

        if outlook == "Very Positive":

            return "Aggressive Growth"

        elif outlook == "Positive":

            return "Growth Opportunity"

        elif outlook == "Neutral":

            return "Monitor"

        return "Defensive Position"

    ###########################################################
    # Run
    ###########################################################

    def run(

        self,

        context,

    ):

        financial_analysis = context.get(

            "financial_analysis",

            {},

        )

        news_analysis = context.get(

            "news_analysis",

            {},

        )

        risk_analysis = context.get(

            "risk_analysis",

            {},

        )

        #######################################################
        # Scores
        #######################################################

        financial_score = (

            financial_analysis.get(

                "investment_strength_score",

                50,

            )

        )

        news_score = (

            news_analysis.get(

                "news_score",

                50,

            )

        )

        risk_score = (

            risk_analysis.get(

                "enterprise_risk_score",

                50,

            )

        )

        #######################################################
        # Forecasts
        #######################################################

        revenue_growth = (

            self.revenue_forecast(

                financial_score,

                news_score,

                risk_score,

            )

        )

        eps_growth = (

            self.eps_forecast(

                revenue_growth

            )

        )

        cash_flow_growth = (

            self.cash_flow_forecast(

                revenue_growth

            )

        )

        margin_growth = (

            self.margin_forecast(

                revenue_growth

            )

        )

        #######################################################
        # Confidence
        #######################################################

        confidence = (

            self.confidence(

                financial_score,

                news_score,

                risk_score,

            )

        )

        #######################################################
        # Scenario Analysis
        #######################################################

        scenarios = (

            self.scenarios(

                revenue_growth

            )

        )

        #######################################################
        # Outlook
        #######################################################

        forecast_outlook = (

            self.outlook(

                revenue_growth

            )

        )

        recommendation = (

            self.recommendation(

                forecast_outlook

            )

        )

        #######################################################
        # Output
        #######################################################

        return {

            "forecasting_analysis": {

                "revenue_growth_forecast":

                    revenue_growth,

                "eps_growth_forecast":

                    eps_growth,

                "cash_flow_growth_forecast":

                    cash_flow_growth,

                "margin_growth_forecast":

                    margin_growth,

                "forecast_confidence":

                    confidence,

                "forecast_outlook":

                    forecast_outlook,

                "recommendation":

                    recommendation,

                "scenarios":

                    scenarios,

            }

        }