from app.portfolio.sector_analyzer import (
    SectorAnalyzer,
)

from app.portfolio.diversification_analyzer import (
    DiversificationAnalyzer,
)

from app.portfolio.concentration_analyzer import (
    ConcentrationAnalyzer,
)

from app.portfolio.correlation_engine import (
    CorrelationEngine,
)

from app.portfolio.portfolio_risk_engine import (
    PortfolioRiskEngine,
)

from app.portfolio.recommendation_engine import (
    RecommendationEngine,
)


class EnterprisePortfolioAdvisor:

    """
    Enterprise AI Portfolio Advisor
    """

    ###########################################################
    # Risk Profile
    ###########################################################

    @staticmethod
    def risk_profile(

        risk_score,

    ):

        if risk_score >= 70:

            return "Aggressive"

        elif risk_score >= 40:

            return "Moderate"

        return "Conservative"

    ###########################################################
    # Portfolio Health
    ###########################################################

    @staticmethod
    def portfolio_health(

        diversification,

        concentration,

        risk_score,

    ):

        score = (

            diversification * 0.4

            +

            (100 - concentration) * 0.3

            +

            (100 - risk_score) * 0.3

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

        health_score,

    ):

        if health_score >= 85:

            return "Excellent"

        elif health_score >= 70:

            return "Strong"

        elif health_score >= 55:

            return "Moderate"

        return "Weak"

    ###########################################################
    # Position Size Recommendation
    ###########################################################

    @staticmethod
    def position_sizing(

        portfolio_df,

    ):

        recommendations = {}

        for _, row in (

            portfolio_df.iterrows()

        ):

            weight = row["weight"]

            symbol = row["symbol"]

            if weight > 25:

                recommendations[

                    symbol

                ] = (

                    "Reduce"

                )

            elif weight < 5:

                recommendations[

                    symbol

                ] = (

                    "Increase"

                )

            else:

                recommendations[

                    symbol

                ] = (

                    "Maintain"

                )

        return recommendations

    ###########################################################
    # Sector Concentration
    ###########################################################

    @staticmethod
    def sector_warnings(

        sector_allocation,

    ):

        warnings = []

        for sector, weight in (

            sector_allocation.items()

        ):

            if weight > 40:

                warnings.append(

                    f"{sector} concentration "

                    f"is high ({weight}%)"

                )

        return warnings

    ###########################################################
    # Rebalancing Suggestions
    ###########################################################

    @staticmethod
    def rebalance(

        sector_allocation,

    ):

        suggestions = []

        for sector, weight in (

            sector_allocation.items()

        ):

            if weight > 40:

                suggestions.append(

                    f"Reduce exposure to "

                    f"{sector}"

                )

        if not suggestions:

            suggestions.append(

                "No major rebalancing required"

            )

        return suggestions

    ###########################################################
    # Main Analysis
    ###########################################################

    @staticmethod
    def analyze(

        portfolio_df,

    ):

        #######################################################
        # Core Metrics
        #######################################################

        sector_allocation = (

            SectorAnalyzer.analyze(

                portfolio_df

            )

        )

        diversification = (

            DiversificationAnalyzer.score(

                portfolio_df

            )

        )

        concentration = (

            ConcentrationAnalyzer.score(

                portfolio_df

            )

        )

        correlation = (

            CorrelationEngine.estimate(

                portfolio_df

            )

        )

        risk_score = (

            PortfolioRiskEngine.score(

                concentration,

                diversification,

                correlation,

            )

        )

        recommendation = (

            RecommendationEngine.generate(

                risk_score

            )

        )

        #######################################################
        # Enterprise Metrics
        #######################################################

        health_score = (

            EnterprisePortfolioAdvisor

            .portfolio_health(

                diversification,

                concentration,

                risk_score,

            )

        )

        rating = (

            EnterprisePortfolioAdvisor

            .investment_rating(

                health_score

            )

        )

        profile = (

            EnterprisePortfolioAdvisor

            .risk_profile(

                risk_score

            )

        )

        position_sizing = (

            EnterprisePortfolioAdvisor

            .position_sizing(

                portfolio_df

            )

        )

        warnings = (

            EnterprisePortfolioAdvisor

            .sector_warnings(

                sector_allocation

            )

        )

        rebalance = (

            EnterprisePortfolioAdvisor

            .rebalance(

                sector_allocation

            )

        )

        #######################################################
        # Output
        #######################################################

        return {

            "portfolio_health_score":

                health_score,

            "investment_rating":

                rating,

            "risk_profile":

                profile,

            "sector_allocation":

                sector_allocation,

            "diversification_score":

                diversification,

            "concentration_score":

                concentration,

            "correlation_estimate":

                correlation,

            "risk_score":

                risk_score,

            "position_sizing":

                position_sizing,

            "sector_warnings":

                warnings,

            "rebalancing_suggestions":

                rebalance,

            "recommendation":

                recommendation,

        }