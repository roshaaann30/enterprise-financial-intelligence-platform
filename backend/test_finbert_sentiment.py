from app.nlp.sentiment.finbert_sentiment import (
    FinBERTSentiment,
)

###########################################################

text = """

Revenue increased by 25%.

Management expects strong growth.

AI initiatives are accelerating.

Profit margins improved significantly.

"""

###########################################################

model = FinBERTSentiment()

result = model.predict(

    text

)

###########################################################

print()

print("=" * 60)

print("FINBERT SENTIMENT")

print("=" * 60)

print()

for key, value in result.items():

    print(

        key,

        ":",

        value,

    )