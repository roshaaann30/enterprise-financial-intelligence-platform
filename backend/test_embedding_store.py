from app.pdf.embeddings.embedding_store import (
    EmbeddingStore,
)

from app.pdf.embeddings.pdf_embedding_engine import (
    PDFEmbeddingEngine,
)

chunks = [

    "Revenue increased.",

    "AI investments continue.",

]

engine = PDFEmbeddingEngine()

embeddings = (

    engine.embed(

        chunks

    )

)

EmbeddingStore.save(

    embeddings,

    "embeddings.npy",

)

loaded = (

    EmbeddingStore.load(

        "embeddings.npy"

    )

)

print(

    loaded.shape

)