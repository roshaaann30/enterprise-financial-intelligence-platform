from app.nlp.outlook.business_outlook import (
    BusinessOutlook,
)

###########################################################

text = """

Management expects continued growth.

Strong demand remains across markets.

Revenue is expected to increase.

The company remains optimistic about
future opportunities.

Margins continue to improve.

"""

###########################################################

result = BusinessOutlook.analyze(

    text

)

###########################################################

print()

print("=" * 60)

print("BUSINESS OUTLOOK")

print("=" * 60)

print()

for key, value in result.items():

    print(

        key,

        ":",

        value,

    )