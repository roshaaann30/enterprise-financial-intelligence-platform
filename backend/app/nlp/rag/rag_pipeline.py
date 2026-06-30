from app.nlp.rag.retriever import (
    FinancialRetriever,
)


class FinancialRAGPipeline:

    """
    Enterprise Financial RAG Pipeline
    """

    @staticmethod
    def ask(

        vector_store,

        question,

        top_k=5,

    ):

        chunks = (

            FinancialRetriever.retrieve(

                vector_store,

                question,

                top_k,

            )

        )

        return {

            "question":

                question,

            "retrieved_chunks":

                chunks,

        }