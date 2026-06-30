from app.nlp.opportunity_extraction.opportunity_extractor import (
    FinancialOpportunityExtractor,
)

###########################################################

text = """

Management expects strong revenue growth.

The company plans international expansion.

AI investments continue to accelerate.

A new product launch is scheduled next quarter.

Strategic partnerships are expanding globally.

"""

###########################################################

results = (

    FinancialOpportunityExtractor.extract(

        text

    )

)

###########################################################

print()

print("=" * 60)

print("OPPORTUNITY EXTRACTION")

print("=" * 60)

print()

for item in results:

    print(

        item

    )