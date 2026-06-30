from app.agents.base_agent import (
    BaseAgent,
)

from app.nlp.rag.rag_pipeline import (
    FinancialRAGPipeline,
)


class ResearchAgent(

    BaseAgent

):

    """
    Research Agent

    Uses:
    - Knowledge Base
    - Financial RAG
    - PDF Intelligence
    """

    ###########################################################
    # Constructor
    ###########################################################

    def __init__(

        self,

    ):

        super().__init__(

            "ResearchAgent"

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

        knowledge = context.get(

            "knowledge",

            {},

        )

        vector_store = context.get(

            "vector_store",

            None,

        )

        query = context.get(

            "query",

            "Provide financial research findings",

        )

        #######################################################
        # RAG Search
        #######################################################

        rag_results = []

        if vector_store is not None:

            try:

                rag_output = (

                    FinancialRAGPipeline.ask(

                        vector_store,

                        query,

                    )

                )

                rag_results = (

                    rag_output.get(

                        "retrieved_chunks",

                        [],

                    )

                )

            except Exception as e:

                rag_results = [

                    f"RAG Error: {str(e)}"

                ]

        #######################################################
        # Research Findings
        #######################################################

        findings = {

            "company":

                knowledge.get(

                    "company"

                ),

            "metrics":

                knowledge.get(

                    "metrics",

                    {},

                ),

            "risks":

                knowledge.get(

                    "risks",

                    [],

                ),

            "opportunities":

                knowledge.get(

                    "opportunities",

                    [],

                ),

            "strategies":

                knowledge.get(

                    "strategies",

                    [],

                ),

            "entities":

                knowledge.get(

                    "entities",

                    [],

                ),

            "outlook":

                knowledge.get(

                    "outlook",

                    {},

                ),

            "rag_findings":

                rag_results,

        }

        #######################################################
        # Return
        #######################################################

        return {

            "research_findings":

                findings

        }