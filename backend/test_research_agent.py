from app.agents.research_agent import (
    ResearchAgent,
)

from app.nlp.rag.vector_store import (
    FinancialVectorStore,
)

###########################################################
# Sample Chunks
###########################################################

chunks = [

    "Revenue increased by 22%.",

    "AI investments remain a strategic priority.",

    "Management expects continued growth.",

    "Supply chain risks remain under monitoring.",

]

###########################################################
# Build RAG Store
###########################################################

store = FinancialVectorStore()

store.build(

    chunks

)

###########################################################
# Knowledge
###########################################################

knowledge = {

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

    "outlook": {

        "outlook":

            "Positive"

    },

}

###########################################################
# Agent
###########################################################

agent = ResearchAgent()

###########################################################
# Run
###########################################################

result = agent.run(

    {

        "knowledge":

            knowledge,

        "vector_store":

            store,

        "query":

            "What did management say about AI?",

    }

)

###########################################################

print()

print("=" * 60)

print("RESEARCH AGENT")

print("=" * 60)

print()

print(

    result

)