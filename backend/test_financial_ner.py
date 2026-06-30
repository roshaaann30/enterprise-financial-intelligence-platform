from app.nlp.entities.financial_ner import (
    FinancialNER,
)

###########################################################

text = """

Microsoft announced new AI investments.

Satya Nadella stated that Azure growth
remains strong.

The company plans expansion across India,
Europe, and North America.

Revenue exceeded $100 billion.

"""

###########################################################

ner = FinancialNER()

results = ner.extract(

    text

)

###########################################################

print()

print("=" * 60)

print("FINANCIAL NER")

print("=" * 60)

print()

for entity in results:

    print(

        entity

    )