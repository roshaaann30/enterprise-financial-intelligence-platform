from app.risk.datasets.bankruptcy_dataset import (
    BankruptcyDataset,
)

from app.risk.preprocessing.bankruptcy_preprocessor import (
    BankruptcyPreprocessor,
)

from app.risk.models.bankruptcy_model import (
    BankruptcyModel,
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

model = BankruptcyModel()

model.fit(

    processed["X_train"],

    processed["y_train"],

)

##############################################################

predictions = model.predict(

    processed["X_test"]

)

probabilities = model.predict_proba(

    processed["X_test"]

)

##############################################################

print()

print("=" * 60)

print("BANKRUPTCY MODEL")

print("=" * 60)

print()

print(

    "Predictions Shape:",

    predictions.shape,

)

print()

print(

    "Probability Shape:",

    probabilities.shape,

)

##############################################################

model.save()

print()

print(

    "Model saved successfully."

)