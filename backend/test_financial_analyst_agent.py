from app.agents.financial_analyst_agent import (
    FinancialAnalystAgent,
)

###########################################################

research_findings = {

    "company":

        "Tesla",

    "metrics": {

        "Revenue":

            "96.7B",

        "Net Income":

            "12.4B",

    },

    "risks": [

        {

            "risk_type":

                "Supply Chain Risk"

        }

    ],

    "opportunities": [

        {

            "opportunity_type":

                "AI Investment"

        },

        {

            "opportunity_type":

                "Market Expansion"

        },

    ],

}

###########################################################

agent = (

    FinancialAnalystAgent()

)

###########################################################

result = (

    agent.run(

        {

            "research_findings":

                research_findings

        }

    )

)

###########################################################

print()

print("=" * 60)

print("FINANCIAL ANALYST AGENT")

print("=" * 60)

print()

print(

    result

)