from app.nlp.ingestion.document_loader import (
    FinancialDocumentLoader,
)

###########################################################

result = FinancialDocumentLoader.load(

    "sample_annual_report.txt"

)

###########################################################

print()

print("=" * 60)

print("DOCUMENT LOADER")

print("=" * 60)

print()

print(

    "File:",

    result["file_name"]

)

print(

    "Type:",

    result["document_type"]

)

print()

print(

    result["text"][:500]

)