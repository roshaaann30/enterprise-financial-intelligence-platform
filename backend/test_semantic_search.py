from app.pdf.embeddings.pdf_embedding_engine import (
    PDFEmbeddingEngine,
)

from app.pdf.embeddings.semantic_search import (
    SemanticSearch,
)

chunks = [

    "Revenue increased significantly.",

    "AI investments remain a priority.",

    "Supply chain disruptions continue.",

]

engine = PDFEmbeddingEngine()

embeddings = (

    engine.embed(

        chunks

    )

)

query = (

    engine.embed_query(

        "What did management say about AI?"

    )

)

results = (

    SemanticSearch.search(

        query,

        embeddings,

        chunks,

    )

)

for item in results:

    print(item)