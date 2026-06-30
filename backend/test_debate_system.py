from app.debate.debate_engine import (
    DebateEngine,
)

from app.debate.decision_agent import (
    DecisionAgent,
)

context = {

    "research_findings": {

        "opportunities": [

            {

                "opportunity_type":

                    "AI Investment"

            },

            {

                "opportunity_type":

                    "Market Expansion"

            }

        ],

        "risks": [

            {

                "risk_type":

                    "Supply Chain Risk"

            }

        ],

        "outlook": {

            "outlook":

                "Positive"

        }

    }

}

###########################################################

debate = (

    DebateEngine.run(

        context

    )

)

###########################################################

decision = (

    DecisionAgent.decide(

        debate

    )

)

###########################################################

print()

print("=" * 60)

print("AI INVESTMENT DEBATE")

print("=" * 60)

print()

print(decision)