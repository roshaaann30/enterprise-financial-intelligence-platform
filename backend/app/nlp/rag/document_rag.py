from app.nlp.ingestion.document_loader import (
    FinancialDocumentLoader,
)

from app.nlp.preprocessing.text_chunker import (
    FinancialTextChunker,
)

from app.nlp.rag.vector_store import (
    FinancialVectorStore,
)


class DocumentRAG:

    """
    Document-Aware Financial RAG
    """

    @staticmethod
    def build(

        file_path,

    ):

        ###################################################
        # Load Document
        ###################################################

        document = (

            FinancialDocumentLoader.load(

                file_path

            )

        )

        ###################################################
        # Chunk
        ###################################################

        chunks = (

            FinancialTextChunker.process(

                text=document["text"],

                source_file=document["file_name"],

                document_type=document["document_type"],

                chunk_size=300,

                overlap=50,

            )

        )

        ###################################################
        # Extract Text
        ###################################################

        texts = [

            chunk["text"]

            for chunk in chunks

        ]

        ###################################################
        # Build Vector Store
        ###################################################

        store = FinancialVectorStore()

        store.build(

            texts

        )

        return {

            "document": document,

            "chunks": chunks,

            "vector_store": store,

        }