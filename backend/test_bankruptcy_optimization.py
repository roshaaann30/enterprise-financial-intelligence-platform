from app.risk.datasets.bankruptcy_dataset import (
    BankruptcyDataset,
)

from app.risk.preprocessing.bankruptcy_preprocessor import (
    BankruptcyPreprocessor,
)

from app.risk.optimization.bankruptcy_optimizer import (
    BankruptcyOptimizer,
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

results = BankruptcyOptimizer.optimize(

    processed["X_train"],

    processed["y_train"],

    processed["X_test"],

    processed["y_test"],

    n_trials=10,

)

##############################################################

print()

print("=" * 60)

print("BANKRUPTCY OPTIMIZATION")

print("=" * 60)

print()

print(

    "Best ROC_AUC:",

    results["best_score"]

)

print()

print(

    "Best Parameters"

)

print(

    results["best_params"]

)