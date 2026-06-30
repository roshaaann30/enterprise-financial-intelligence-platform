from app.risk.datasets.credit_dataset import (
    CreditDataset,
)

from app.risk.preprocessing.credit_preprocessor import (
    CreditPreprocessor,
)

from app.risk.models.credit_risk_model import (
    CreditRiskModel,
)

from app.risk.explainability.credit_shap import (
    CreditSHAP,
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

sample = data["X"].iloc[[0]]

###########################################################

explainer = CreditSHAP(

    model.model

)

###########################################################

results = explainer.explain(

    sample,

    top_n=10,

)

###########################################################

print()

print("=" * 60)

print("TOP CREDIT SHAP FEATURES")

print("=" * 60)

print()

for item in results:

    print(

        item["Feature"],

        "=>",

        round(

            item["Impact"],

            4,

        ),

    )