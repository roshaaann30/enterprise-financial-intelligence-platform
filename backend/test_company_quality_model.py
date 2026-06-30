import pandas as pd

from sklearn.model_selection import (
    train_test_split,
)

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)

from app.risk.models.company_quality_model import (
    CompanyQualityModel,
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

model = CompanyQualityModel()

model.fit(

    X_train,

    y_train,

)

###########################################################

predictions = model.predict(

    X_test

)

###########################################################

mae = mean_absolute_error(

    y_test,

    predictions,

)

rmse = mean_squared_error(

    y_test,

    predictions,

) ** 0.5

r2 = r2_score(

    y_test,

    predictions,

)

###########################################################

print()

print("=" * 60)

print("COMPANY QUALITY MODEL")

print("=" * 60)

print()

print(

    "MAE:",

    round(mae, 4),

)

print(

    "RMSE:",

    round(rmse, 4),

)

print(

    "R2:",

    round(r2, 4),

)

###########################################################

model.save()

print()

print(

    "Model Saved Successfully"

)