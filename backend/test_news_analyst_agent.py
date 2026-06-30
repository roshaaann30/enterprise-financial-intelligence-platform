from app.agents.news_analyst_agent import (
    NewsAnalystAgent,
)

###########################################################

research_findings = {

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

    "sentiment": {

        "sentiment":

            "Positive"

    }

}

###########################################################

agent = NewsAnalystAgent()

###########################################################

result = agent.run(

    {

        "research_findings":

            research_findings

    }

)

###########################################################

print()

print("=" * 60)

print("NEWS ANALYST AGENT")

print("=" * 60)

print()

print(result)