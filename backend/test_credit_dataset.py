from app.risk.datasets.credit_dataset import (
    CreditDataset,
)

###########################################################

dataset = CreditDataset()

result = dataset.process()

###########################################################

print()

print("=" * 60)

print("CREDIT DATASET")

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