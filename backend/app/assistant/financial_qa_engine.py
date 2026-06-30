from app.pdf.embeddings.pdf_embedding_engine import (
    PDFEmbeddingEngine,
)

from app.pdf.embeddings.semantic_search import (
    SemanticSearch,
)

from app.assistant.citation_engine import (
    CitationEngine,
)


class FinancialQAEngine:

    """
    Financial Question Answering Engine
    """

    @staticmethod
    def ask(

        question,

        chunks,

        top_k=3,

    ):

        #######################################################
        # Embeddings
        #######################################################

        engine = (

            PDFEmbeddingEngine()

        )

        embeddings = (

            engine.embed(

                chunks

            )

        )

        query_embedding = (

            engine.embed_query(

                question

            )

        )

        #######################################################
        # Retrieval
        #######################################################

        results = (

            SemanticSearch.search(

                query_embedding,

                embeddings,

                chunks,

                top_k,

            )

        )

        #######################################################
        # Context
        #######################################################

        retrieved_chunks = [

            item["chunk"]

            for item in results

        ]

        answer = "\n\n".join(

            retrieved_chunks

        )

        #######################################################
        # Citations
        #######################################################

        citations = (

            CitationEngine.build(

                retrieved_chunks

            )

        )

        #######################################################
        # Output
        #######################################################

        return {

            "question":

                question,

            "answer":

                answer,

            "citations":

                citations,

            "confidence":

                90,

        }