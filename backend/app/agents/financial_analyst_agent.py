from app.agents.base_agent import (
    BaseAgent,
)


class FinancialAnalystAgent(

    BaseAgent

):

    """
    Financial Analyst Agent
    """

    ###########################################################
    # Constructor
    ###########################################################

    def __init__(

        self,

    ):

        super().__init__(

            "FinancialAnalystAgent"

        )

    ###########################################################
    # Calculate Score
    ###########################################################

    @staticmethod
    def calculate_score(

        metrics,

        risks,

        opportunities,

    ):

        score = 50

        score += (

            len(

                opportunities

            ) * 10

        )

        score -= (

            len(

                risks

            ) * 5

        )

        return max(

            0,

            min(

                score,

                100,

            ),

        )

    ###########################################################
    # Classify Health
    ###########################################################

    @staticmethod
    def classify(

        score,

    ):

        if score >= 80:

            return "Excellent"

        elif score >= 65:

            return "Strong"

        elif score >= 50:

            return "Moderate"

        else:

            return "Weak"

    ###########################################################
    # Run
    ###########################################################

    def run(

        self,

        context,

    ):

        research = context.get(

            "research_findings",

            {},

        )

        #######################################################
        # Extract Inputs
        #######################################################

        metrics = research.get(

            "metrics",

            {},

        )

        risks = research.get(

            "risks",

            [],

        )

        opportunities = research.get(

            "opportunities",

            [],

        )

        #######################################################
        # Key Metrics
        #######################################################

        revenue = metrics.get(

            "Revenue",

            "Unknown",

        )

        net_income = metrics.get(

            "Net Income",

            "Unknown",

        )

        #######################################################
        # Financial Score
        #######################################################

        score = self.calculate_score(

            metrics,

            risks,

            opportunities,

        )

        #######################################################
        # Health Classification
        #######################################################

        health = self.classify(

            score

        )

        #######################################################
        # Output
        #######################################################

        return {

            "financial_analysis": {

                "financial_health":

                    health,

                "investment_strength_score":

                    score,

                "metric_count":

                    len(

                        metrics

                    ),

                "risk_count":

                    len(

                        risks

                    ),

                "opportunity_count":

                    len(

                        opportunities

                    ),

                "key_metrics": {

                    "Revenue":

                        revenue,

                    "Net Income":

                        net_income,

                },

            }

        }