from app.risk.datasets.investment_dataset import (
    InvestmentDataset,
)

from app.risk.preprocessing.investment_preprocessor import (
    InvestmentPreprocessor,
)

###########################################################

dataset = InvestmentDataset()

data = dataset.process()

###########################################################

preprocessor = InvestmentPreprocessor()

result = preprocessor.process(

    data["X"],

    data["y"],

)

###########################################################

print()

print("=" * 60)

print("INVESTMENT PREPROCESSING")

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