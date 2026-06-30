from app.risk.datasets.investment_dataset import (
    InvestmentDataset,
)

from app.risk.preprocessing.investment_preprocessor import (
    InvestmentPreprocessor,
)

from app.risk.models.investment_risk_model import (
    InvestmentRiskModel,
)

from app.risk.explainability.investment_shap import (
    InvestmentSHAP,
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

model = InvestmentRiskModel()

model.fit(

    processed["X_train"],

    processed["y_train"],

)

###########################################################

features = preprocessor.generate_features(

    data["X"]

)

sample = features.iloc[[0]]

###########################################################

explainer = InvestmentSHAP(

    model.model

)

results = explainer.explain(

    sample,

    top_n=10,

)

###########################################################

print()

print("=" * 60)

print("INVESTMENT SHAP")

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