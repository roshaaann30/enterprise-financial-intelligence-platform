from app.agents.base_agent import (
    BaseAgent,
)


class RiskAnalystAgent(

    BaseAgent

):

    """
    Enterprise Risk Analyst Agent
    """

    ###########################################################
    # Constructor
    ###########################################################

    def __init__(

        self,

    ):

        super().__init__(

            "RiskAnalystAgent"

        )

    ###########################################################
    # Risk Level
    ###########################################################

    @staticmethod
    def classify(

        score,

    ):

        if score >= 75:

            return "Critical"

        elif score >= 60:

            return "High"

        elif score >= 35:

            return "Moderate"

        else:

            return "Low"

    ###########################################################
    # Recommendation
    ###########################################################

    @staticmethod
    def recommendation(

        level,

    ):

        if level == "Critical":

            return (

                "Immediate Attention Required"

            )

        elif level == "High":

            return (

                "Monitor Closely"

            )

        elif level == "Moderate":

            return (

                "Manage Risk"

            )

        return (

            "Acceptable Risk"

        )

    ###########################################################
    # Enterprise Risk Score
    ###########################################################

    @staticmethod
    def calculate_enterprise_score(

        bankruptcy_score,

        credit_score,

        pdf_risk_score,

        news_score,

    ):

        return round(

            (

                bankruptcy_score * 0.30

                +

                credit_score * 0.25

                +

                pdf_risk_score * 0.20

                +

                news_score * 0.25

            ),

            2,

        )

    ###########################################################
    # Run
    ###########################################################

    def run(

        self,

        context,

    ):

        #######################################################
        # Inputs
        #######################################################

        bankruptcy_score = context.get(

            "bankruptcy_score",

            50,

        )

        credit_score = context.get(

            "credit_score",

            50,

        )

        pdf_risk_score = context.get(

            "pdf_risk_score",

            50,

        )

        news_analysis = context.get(

            "news_analysis",

            {},

        )

        news_score = news_analysis.get(

            "news_score",

            50,

        )

        research = context.get(

            "research_findings",

            {},

        )

        risks = research.get(

            "risks",

            [],

        )

        #######################################################
        # Enterprise Score
        #######################################################

        enterprise_score = (

            self.calculate_enterprise_score(

                bankruptcy_score,

                credit_score,

                pdf_risk_score,

                news_score,

            )

        )

        #######################################################
        # Classification
        #######################################################

        risk_level = (

            self.classify(

                enterprise_score

            )

        )

        recommendation = (

            self.recommendation(

                risk_level

            )

        )

        #######################################################
        # Output
        #######################################################

        return {

            "risk_analysis": {

                "enterprise_risk_score":

                    enterprise_score,

                "risk_level":

                    risk_level,

                "recommendation":

                    recommendation,

                "bankruptcy_score":

                    bankruptcy_score,

                "credit_score":

                    credit_score,

                "pdf_risk_score":

                    pdf_risk_score,

                "news_score":

                    news_score,

                "risk_count":

                    len(

                        risks

                    ),

                "key_risks":

                    risks,

            }

        }