from app.nlp.ingestion.document_loader import (
    FinancialDocumentLoader,
)

from app.nlp.preprocessing.text_chunker import (
    FinancialTextChunker,
)

###########################################################

document = FinancialDocumentLoader.load(

    "sample_annual_report.txt"

)

###########################################################

chunks = FinancialTextChunker.process(

    text=document["text"],

    source_file=document["file_name"],

    document_type=document["document_type"],

    chunk_size=20,

    overlap=5,

)

###########################################################

print()

print("=" * 60)

print("TEXT CHUNKER")

print("=" * 60)

print()

print(

    "Total Chunks:",

    len(chunks)

)

print()

for chunk in chunks:

    print(

        f"Chunk {chunk['chunk_id']}"

    )

    print(

        chunk["text"]

    )

    print()