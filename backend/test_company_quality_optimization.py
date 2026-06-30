import pandas as pd

from sklearn.model_selection import (
    train_test_split,
)

from app.risk.optimization.company_quality_optimizer import (
    CompanyQualityOptimizer,
)

###########################################################

df = pd.read_csv(

    "datasets/risk/company_quality.csv"

)

###########################################################

X = df[

    [

        "FinancialHealth",

        "BankruptcyRisk",

        "CreditRisk",

        "InvestmentScore",

    ]

]

y = df["QualityScore"]

###########################################################

X_train, X_test, y_train, y_test = (

    train_test_split(

        X,

        y,

        test_size=0.2,

        random_state=42,

    )

)

###########################################################

results = (

    CompanyQualityOptimizer.optimize(

        X_train,

        y_train,

        X_test,

        y_test,

        n_trials=10,

    )

)

###########################################################

print()

print("=" * 60)

print("COMPANY QUALITY OPTIMIZATION")

print("=" * 60)

print()

print(

    "Best RMSE:",

    results["best_rmse"]

)

print()

print(

    results["best_params"]

)