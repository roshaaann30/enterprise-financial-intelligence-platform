from app.agents.risk_analyst_agent import (
    RiskAnalystAgent,
)

agent = RiskAnalystAgent()

result = agent.run(

    {

        "bankruptcy_score": 70,

        "credit_score": 65,

        "pdf_risk_score": 60,

        "news_analysis": {

            "news_score": 75,

        },

        "research_findings": {

            "risks": [

                {

                    "risk_type":

                        "Supply Chain Risk"

                },

                {

                    "risk_type":

                        "Cybersecurity Risk"

                }

            ]

        }

    }

)

print(result)