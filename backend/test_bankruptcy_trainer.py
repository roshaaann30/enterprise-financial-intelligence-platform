from app.risk.datasets.bankruptcy_dataset import (
    BankruptcyDataset,
)

from app.risk.preprocessing.bankruptcy_preprocessor import (
    BankruptcyPreprocessor,
)

from app.risk.models.bankruptcy_model import (
    BankruptcyModel,
)

from app.risk.trainers.bankruptcy_trainer import (
    BankruptcyTrainer,
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

trainer = BankruptcyTrainer(

    model,

)

##############################################################

trainer.train(

    processed["X_train"],

    processed["y_train"],

)

##############################################################

results = trainer.evaluate(

    processed["X_test"],

    processed["y_test"],

)

##############################################################

print()

print("=" * 60)

print("BANKRUPTCY MODEL EVALUATION")

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