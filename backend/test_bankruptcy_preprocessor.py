from app.risk.datasets.bankruptcy_dataset import (
    BankruptcyDataset,
)

from app.risk.preprocessing.bankruptcy_preprocessor import (
    BankruptcyPreprocessor,
)

##############################################################

dataset = BankruptcyDataset()

data = dataset.process()

##############################################################

preprocessor = BankruptcyPreprocessor()

result = preprocessor.process(

    data["X"],

    data["y"],

)

##############################################################

print()

print("=" * 60)

print("BANKRUPTCY PREPROCESSING")

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

    "Class Distribution"

)

print(

    result["distribution"]

)