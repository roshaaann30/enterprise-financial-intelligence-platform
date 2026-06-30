from app.pdf.risk_analysis.pdf_risk_pipeline import (
    PDFRiskPipeline,
)

###########################################################

sample_text = """

Risk Factors

Supply chain disruptions remain a concern.

Inflation and market volatility continue.

Cybersecurity threats are increasing.

Competition from new entrants may impact
future growth.

"""

###########################################################

result = (

    PDFRiskPipeline.analyze(

        sample_text

    )

)

###########################################################

print()

print("=" * 60)

print("PDF RISK INTELLIGENCE")

print("=" * 60)

print()

for key, value in result.items():

    print(

        key,

        ":",

        value,

    )