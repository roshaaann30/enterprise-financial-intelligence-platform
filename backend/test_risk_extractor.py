from app.nlp.risk_extraction.risk_extractor import (
    FinancialRiskExtractor,
)

###########################################################

text = """

The company continues to face supply chain
disruptions and vendor shortages.

Management remains concerned about inflation
and market volatility.

Cybersecurity threats continue to increase.

Competition from new entrants may impact
future market share.

"""

###########################################################

results = FinancialRiskExtractor.extract(

    text

)

###########################################################

print()

print("=" * 60)

print("FINANCIAL RISK EXTRACTION")

print("=" * 60)

print()

for risk in results:

    print(

        risk

    )