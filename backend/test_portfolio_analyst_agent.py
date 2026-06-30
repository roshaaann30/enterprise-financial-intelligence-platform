from app.agents.portfolio_analyst_agent import (
    PortfolioAnalystAgent,
)

agent = PortfolioAnalystAgent()

result = agent.run(

    {

        "financial_analysis": {

            "investment_strength_score":

                80,

        },

        "news_analysis": {

            "news_score":

                75,

        },

        "risk_analysis": {

            "enterprise_risk_score":

                35,

            "risk_level":

                "Moderate",

        },

        "forecasting_analysis": {

            "forecast_confidence":

                78,

        },

    }

)

print()

print("=" * 60)

print("PORTFOLIO ANALYST AGENT")

print("=" * 60)

print()

print(result)