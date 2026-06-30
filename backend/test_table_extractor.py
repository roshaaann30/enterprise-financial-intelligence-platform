from app.pdf.tables.table_extractor import (
    FinancialTableExtractor,
)

###########################################################

tables = (

    FinancialTableExtractor.extract(

        "sample_report.pdf"

    )

)

###########################################################

print()

print("=" * 60)

print("TABLE EXTRACTION")

print("=" * 60)

print()

print(

    "Tables Found:",

    len(tables)

)

print()

if tables:

    print(

        tables[0]["data"]

    )

else:

    print(

        "No tables found."

    )