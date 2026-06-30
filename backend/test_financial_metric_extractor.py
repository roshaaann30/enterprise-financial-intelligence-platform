from app.pdf.tables.table_extractor import (
    FinancialTableExtractor,
)

from app.pdf.metrics.financial_metric_extractor import (
    FinancialMetricExtractor,
)

###########################################################

tables = (

    FinancialTableExtractor.extract(

        "sample_report.pdf"

    )

)

###########################################################

metrics = (

    FinancialMetricExtractor.extract_from_tables(

        tables

    )

)

###########################################################

print()

print("=" * 60)

print("FINANCIAL METRIC EXTRACTION")

print("=" * 60)

print()

for key, value in metrics.items():

    print(

        key,

        ":",

        value,

    )