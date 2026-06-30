from app.pdf.embeddings.pdf_embedding_engine import (
    PDFEmbeddingEngine,
)

from app.pdf.qa.pdf_qa_engine import (
    PDFQAEngine,
)

###########################################################

chunks = [

    "Revenue increased by 22%.",

    "AI investments remain a strategic priority.",

    "Management expects continued growth.",

    "Supply chain risks remain under monitoring.",

]

###########################################################

engine = (

    PDFEmbeddingEngine()

)

embeddings = (

    engine.embed(

        chunks

    )

)

###########################################################

question = (

    "What did management say about AI?"

)

query_embedding = (

    engine.embed_query(

        question

    )

)

###########################################################

result = (

    PDFQAEngine.answer(

        question,

        query_embedding,

        embeddings,

        chunks,

    )

)

###########################################################

print()

print("=" * 60)

print("PDF QUESTION ANSWERING")

print("=" * 60)

print()

print(

    "Question:",

    result["question"]

)

print()

print(

    "Answer:\n"

)

print(

    result["answer"]

)