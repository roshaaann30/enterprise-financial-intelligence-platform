from app.nlp.rag.vector_store import (
    FinancialVectorStore,
)

from app.nlp.rag.rag_pipeline import (
    FinancialRAGPipeline,
)

###########################################################

chunks = [

    "The company faces supply chain risks.",

    "AI investments increased significantly.",

    "Management expects strong revenue growth.",

    "Cybersecurity remains a key concern.",

    "The company plans expansion into Asia.",

]

###########################################################

store = FinancialVectorStore()

store.build(

    chunks

)

###########################################################

result = FinancialRAGPipeline.ask(

    store,

    "What did management say about AI?",

)

###########################################################

print()

print("=" * 60)

print("FINANCIAL RAG")

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