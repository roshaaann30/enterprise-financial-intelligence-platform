from app.pdf.embeddings.semantic_search import (
    SemanticSearch,
)


class PDFQAEngine:

    """
    Enterprise PDF QA Engine
    """

    @staticmethod
    def answer(

        question,

        query_embedding,

        embeddings,

        chunks,

        top_k=3,

    ):

        results = (

            SemanticSearch.search(

                query_embedding,

                embeddings,

                chunks,

                top_k,

            )

        )

        context = "\n\n".join(

            item["chunk"]

            for item in results

        )

        return {

            "question":

                question,

            "answer":

                context,

            "sources":

                results,

        }