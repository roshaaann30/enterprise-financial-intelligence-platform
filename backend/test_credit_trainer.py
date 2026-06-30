from app.risk.datasets.credit_dataset import (
    CreditDataset,
)

from app.risk.preprocessing.credit_preprocessor import (
    CreditPreprocessor,
)

from app.risk.models.credit_risk_model import (
    CreditRiskModel,
)

from app.risk.trainers.credit_trainer import (
    CreditTrainer,
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

trainer = CreditTrainer(

    model,

)

###########################################################

trainer.train(

    processed["X_train"],

    processed["y_train"],

)

###########################################################

results = trainer.evaluate(

    processed["X_test"],

    processed["y_test"],

)

###########################################################

print()

print("=" * 60)

print("CREDIT RISK EVALUATION")

print("=" * 60)

print()

for metric, value in results["metrics"].items():

    print(

        f"{metric}: {value:.4f}"

    )

print()

print("Confusion Matrix")

print(

    results["confusion_matrix"]

)