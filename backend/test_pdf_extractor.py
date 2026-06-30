from app.pdf.extraction.pdf_extractor import (
    PDFExtractor,
)

###########################################################

result = PDFExtractor.extract(

    "sample_report.pdf"

)

###########################################################

print()

print("=" * 60)

print("PDF EXTRACTION")

print("=" * 60)

print()

print(

    "File:",

    result["file_name"]

)

print(

    "Pages:",

    result["page_count"]

)

print()

print(

    "Metadata:",

    result["metadata"]

)

print()

print(

    result["text"][:1000]

)