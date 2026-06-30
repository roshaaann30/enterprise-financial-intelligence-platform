from app.agents.base_agent import (
    BaseAgent,
)


class PortfolioAnalystAgent(

    BaseAgent

):

    """
    Enterprise Portfolio Analyst Agent
    """

    ###########################################################
    # Constructor
    ###########################################################

    def __init__(

        self,

    ):

        super().__init__(

            "PortfolioAnalystAgent"

        )

    ###########################################################
    # Portfolio Fit Score
    ###########################################################

    @staticmethod
    def portfolio_fit_score(

        financial_score,

        news_score,

        risk_score,

        forecast_confidence,

    ):

        score = (

            financial_score * 0.35

            +

            news_score * 0.25

            +

            (100 - risk_score) * 0.25

            +

            forecast_confidence * 0.15

        )

        return round(

            score,

            2,

        )

    ###########################################################
    # Investment Rating
    ###########################################################

    @staticmethod
    def investment_rating(

        score,

    ):

        if score >= 85:

            return "Strong Buy"

        elif score >= 70:

            return "Buy"

        elif score >= 55:

            return "Hold"

        elif score >= 40:

            return "Reduce"

        return "Sell"

    ###########################################################
    # Risk Profile
    ###########################################################

    @staticmethod
    def risk_profile(

        risk_level,

    ):

        mapping = {

            "Low":

                "Conservative",

            "Moderate":

                "Balanced",

            "High":

                "Aggressive",

            "Critical":

                "Speculative",

        }

        return mapping.get(

            risk_level,

            "Balanced",

        )

    ###########################################################
    # Position Size
    ###########################################################

    @staticmethod
    def position_size(

        score,

    ):

        if score >= 85:

            return "10%"

        elif score >= 70:

            return "8%"

        elif score >= 55:

            return "5%"

        elif score >= 40:

            return "3%"

        return "0%"

    ###########################################################
    # Risk Adjusted Return
    ###########################################################

    @staticmethod
    def risk_adjusted_return(

        forecast_growth,

        risk_score,

    ):

        value = (

            forecast_growth

            *

            (100 - risk_score)

            / 100

        )

        return round(

            value,

            2,

        )

    ###########################################################
    # Sharpe Estimate
    ###########################################################

    @staticmethod
    def sharpe_ratio(

        risk_adjusted_return,

    ):

        return round(

            risk_adjusted_return

            / 10,

            2,

        )

    ###########################################################
    # Volatility Estimate
    ###########################################################

    @staticmethod
    def volatility(

        risk_score,

    ):

        return round(

            risk_score * 0.30,

            2,

        )

    ###########################################################
    # Recommendation
    ###########################################################

    @staticmethod
    def recommendation(

        rating,

    ):

        recommendations = {

            "Strong Buy":

                "High Conviction Investment",

            "Buy":

                "Suitable For Portfolio Inclusion",

            "Hold":

                "Maintain Current Position",

            "Reduce":

                "Reduce Exposure",

            "Sell":

                "Exit Position",

        }

        return recommendations.get(

            rating,

            "Monitor",

        )

    ###########################################################
    # Run
    ###########################################################

    def run(

        self,

        context,

    ):

        financial = context.get(

            "financial_analysis",

            {},

        )

        news = context.get(

            "news_analysis",

            {},

        )

        risk = context.get(

            "risk_analysis",

            {},

        )

        forecast = context.get(

            "forecasting_analysis",

            {},

        )

        #######################################################
        # Inputs
        #######################################################

        financial_score = (

            financial.get(

                "investment_strength_score",

                50,

            )

        )

        news_score = (

            news.get(

                "news_score",

                50,

            )

        )

        risk_score = (

            risk.get(

                "enterprise_risk_score",

                50,

            )

        )

        risk_level = (

            risk.get(

                "risk_level",

                "Moderate",

            )

        )

        forecast_confidence = (

            forecast.get(

                "forecast_confidence",

                50,

            )

        )

        revenue_forecast = (

            forecast.get(

                "revenue_growth_forecast",

                10,

            )

        )

        #######################################################
        # Portfolio Score
        #######################################################

        fit_score = (

            self.portfolio_fit_score(

                financial_score,

                news_score,

                risk_score,

                forecast_confidence,

            )

        )

        #######################################################
        # Analytics
        #######################################################

        rating = (

            self.investment_rating(

                fit_score

            )

        )

        profile = (

            self.risk_profile(

                risk_level

            )

        )

        position_size = (

            self.position_size(

                fit_score

            )

        )

        risk_adjusted_return = (

            self.risk_adjusted_return(

                revenue_forecast,

                risk_score,

            )

        )

        sharpe = (

            self.sharpe_ratio(

                risk_adjusted_return

            )

        )

        volatility = (

            self.volatility(

                risk_score

            )

        )

        recommendation = (

            self.recommendation(

                rating

            )

        )

        #######################################################
        # Output
        #######################################################

        return {

            "portfolio_analysis": {

                "portfolio_fit_score":

                    fit_score,

                "investment_rating":

                    rating,

                "risk_profile":

                    profile,

                "recommended_position_size":

                    position_size,

                "sector_allocation":

                    "Dynamic",

                "risk_adjusted_return":

                    risk_adjusted_return,

                "estimated_sharpe_ratio":

                    sharpe,

                "estimated_volatility":

                    volatility,

                "recommendation":

                    recommendation,

            }

        }