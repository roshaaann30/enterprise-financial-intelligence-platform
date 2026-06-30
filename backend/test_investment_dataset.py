from app.risk.datasets.investment_dataset import (
    InvestmentDataset,
)

###########################################################

dataset = InvestmentDataset()

result = dataset.process()

###########################################################

print()

print("=" * 60)

print("INVESTMENT DATASET")

print("=" * 60)

print()

print(

    result["data"].head()

)

print()

print(

    "Dataset Shape:",

    result["data"].shape,

)

print()

print(

    "Feature Shape:",

    result["X"].shape,

)

print()

print(

    "Target Shape:",

    result["y"].shape,

)