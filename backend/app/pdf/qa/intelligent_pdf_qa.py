from app.pdf.embeddings.pdf_embedding_engine import (
    PDFEmbeddingEngine,
)

from app.pdf.qa.pdf_qa_engine import (
    PDFQAEngine,
)


class IntelligentPDFQA:

    """
    End-to-End PDF QA
    """

    @staticmethod
    def ask(

        question,

        chunks,

    ):

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

        return (

            PDFQAEngine.answer(

                question,

                query_embedding,

                embeddings,

                chunks,

            )

        )