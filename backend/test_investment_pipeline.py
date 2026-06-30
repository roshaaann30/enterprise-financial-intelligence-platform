from app.risk.datasets.investment_dataset import (
    InvestmentDataset,
)

from app.risk.pipeline.investment_pipeline import (
    InvestmentPipeline,
)

###########################################################

dataset = InvestmentDataset()

data = dataset.process()

###########################################################

sample = data["X"].iloc[[0]]

###########################################################

result = InvestmentPipeline.predict(

    sample

)

###########################################################

print()

print("=" * 60)

print("INVESTMENT PIPELINE")

print("=" * 60)

print()

for key, value in result.items():

    print(

        f"{key}: {value}"

    )