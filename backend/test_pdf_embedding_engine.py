from app.pdf.embeddings.pdf_embedding_engine import (
    PDFEmbeddingEngine,
)

chunks = [

    "Revenue increased by 22%.",

    "AI investments remain a strategic priority.",

    "Supply chain risks remain under monitoring.",

]

engine = (

    PDFEmbeddingEngine()

)

embeddings = (

    engine.embed(

        chunks

    )

)

print()

print("=" * 60)

print("PDF EMBEDDINGS")

print("=" * 60)

print()

print(

    "Shape:",

    embeddings.shape,

)

print()

print(

    embeddings[0][:10]

)