from app.risk.datasets.investment_dataset import (
    InvestmentDataset,
)

from app.risk.preprocessing.investment_preprocessor import (
    InvestmentPreprocessor,
)

from app.risk.optimization.investment_optimizer import (
    InvestmentOptimizer,
)

###########################################################

dataset = InvestmentDataset()

data = dataset.process()

###########################################################

preprocessor = InvestmentPreprocessor()

processed = preprocessor.process(

    data["X"],
    data["y"],

)

###########################################################

results = InvestmentOptimizer.optimize_risk(

    processed["X_train"],
    processed["y_train"],

    processed["X_test"],
    processed["y_test"],

    n_trials=10,

)

###########################################################

print()

print("=" * 60)

print("INVESTMENT OPTIMIZATION")

print("=" * 60)

print()

print(

    "Best Score:",

    results["best_score"]

)

print()

print(

    results["best_params"]

)