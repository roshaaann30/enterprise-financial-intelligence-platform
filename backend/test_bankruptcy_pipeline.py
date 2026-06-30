from app.risk.datasets.bankruptcy_dataset import (
    BankruptcyDataset,
)

from app.risk.preprocessing.bankruptcy_preprocessor import (
    BankruptcyPreprocessor,
)

from app.risk.pipeline.bankruptcy_pipeline import (
    BankruptcyPipeline,
)

##############################################################

dataset = BankruptcyDataset()

data = dataset.process()

##############################################################

preprocessor = BankruptcyPreprocessor()

processed = preprocessor.process(

    data["X"],

    data["y"],

)

##############################################################

sample = data["X"].iloc[[0]]

##############################################################

result = BankruptcyPipeline.predict(

    sample

)

##############################################################

print()

print("=" * 60)

print("BANKRUPTCY PREDICTION")

print("=" * 60)

print()

for key, value in result.items():

    print(

        f"{key}: {value}"

    )