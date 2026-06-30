from app.risk.datasets.credit_dataset import (
    CreditDataset,
)

from app.risk.preprocessing.credit_preprocessor import (
    CreditPreprocessor,
)

###########################################################

dataset = CreditDataset()

data = dataset.process()

###########################################################

preprocessor = CreditPreprocessor()

result = preprocessor.process(

    data["X"],

    data["y"],

)

###########################################################

print()

print("=" * 60)

print("CREDIT PREPROCESSING")

print("=" * 60)

print()

print(

    "Train Shape:",

    result["X_train"].shape,

)

print(

    "Test Shape:",

    result["X_test"].shape,

)

print()

print(

    result["distribution"]

)