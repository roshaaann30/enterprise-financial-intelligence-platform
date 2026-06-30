from app.nlp.rag.document_rag import (
    DocumentRAG,
)

from app.nlp.rag.rag_pipeline import (
    FinancialRAGPipeline,
)

###########################################################

rag = DocumentRAG.build(

    "sample_annual_report.txt"

)

###########################################################

result = FinancialRAGPipeline.ask(

    rag["vector_store"],

    "What did management say about AI?",

)

###########################################################

print()

print("=" * 60)

print("DOCUMENT RAG")

print("=" * 60)

print()

print(

    "Question:",

    result["question"]

)

print()

for chunk in result[

    "retrieved_chunks"

]:

    print(

        "-",

        chunk

    )