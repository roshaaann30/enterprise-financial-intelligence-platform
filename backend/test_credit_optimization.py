from app.risk.datasets.credit_dataset import (
    CreditDataset,
)

from app.risk.preprocessing.credit_preprocessor import (
    CreditPreprocessor,
)

from app.risk.optimization.credit_optimizer import (
    CreditOptimizer,
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

results = CreditOptimizer.optimize(

    processed["X_train"],

    processed["y_train"],

    processed["X_test"],

    processed["y_test"],

    n_trials=10,

)

###########################################################

print()

print("=" * 60)

print("CREDIT OPTIMIZATION")

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