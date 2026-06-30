from app.agents.forecasting_agent import (
    ForecastingAgent,
)

agent = ForecastingAgent()

result = agent.run(

    {

        "financial_analysis": {

            "investment_strength_score":

                75,

        },

        "news_analysis": {

            "news_score":

                80,

        },

        "risk_analysis": {

            "enterprise_risk_score":

                40,

        },

    }

)

print()

print("=" * 60)

print("FORECASTING AGENT")

print("=" * 60)

print()

print(result)