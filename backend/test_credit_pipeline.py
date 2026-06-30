from app.risk.datasets.credit_dataset import (
    CreditDataset,
)

from app.risk.preprocessing.credit_preprocessor import (
    CreditPreprocessor,
)

from app.risk.pipeline.credit_pipeline import (
    CreditPipeline,
)

###########################################################

dataset = CreditDataset()

data = dataset.process()

###########################################################

preprocessor = CreditPreprocessor()

processed = preprocessor.process(

    data["X"],

    data["y"],

)

###########################################################

sample = data["X"].iloc[[0]]

###########################################################

result = CreditPipeline.predict(
    sample
)

###########################################################

print()

print("=" * 60)

print("CREDIT RISK PREDICTION")

print("=" * 60)

print()

for key, value in result.items():

    print(
        f"{key}: {value}"
    )