from app.risk.datasets.credit_dataset import (
    CreditDataset,
)

from app.risk.preprocessing.credit_preprocessor import (
    CreditPreprocessor,
)

from app.risk.models.credit_risk_model import (
    CreditRiskModel,
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

model = CreditRiskModel()

model.fit(

    processed["X_train"],

    processed["y_train"],

)

###########################################################

predictions = model.predict(

    processed["X_test"]

)

probabilities = model.predict_proba(

    processed["X_test"]

)

###########################################################

print()

print("=" * 60)

print("CREDIT RISK MODEL")

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

###########################################################

model.save()

print()

print(

    "Model saved successfully."

)