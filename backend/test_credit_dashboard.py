from app.risk.datasets.credit_dataset import (
    CreditDataset,
)

from app.risk.preprocessing.credit_preprocessor import (
    CreditPreprocessor,
)

from app.risk.models.credit_risk_model import (
    CreditRiskModel,
)

from app.risk.pipeline.credit_pipeline import (
    CreditPipeline,
)

from app.risk.explainability.credit_shap import (
    CreditSHAP,
)

from app.risk.dashboard.credit_dashboard import (
    CreditDashboard,
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

model.save()

###########################################################

sample = data["X"].iloc[[0]]

###########################################################

prediction = CreditPipeline.predict(

    sample

)

###########################################################

explainer = CreditSHAP(

    model.model

)

shap_results = explainer.explain(

    sample,

    top_n=5,

)

###########################################################

dashboard = CreditDashboard.borrower_report(

    prediction,

    shap_results,

)

###########################################################

print()

print("=" * 60)

print("CREDIT DASHBOARD")

print("=" * 60)

print()

for key, value in dashboard.items():

    print(

        key,

        ":",

        value,

    )