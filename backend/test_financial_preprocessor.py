from app.nlp.preprocessing.financial_preprocessor import (
    FinancialTextPreprocessor,
)

sample = """

Annual Report 2025

Revenue increased by 22%.

AI investments remain a strategic priority.

Contact: investor@company.com

https://company.com

EBITDA increased by 15%.

"""

processed = FinancialTextPreprocessor.process(

    sample

)

print()

print("=" * 60)

print("FINANCIAL PREPROCESSOR")

print("=" * 60)

print()

print(processed)