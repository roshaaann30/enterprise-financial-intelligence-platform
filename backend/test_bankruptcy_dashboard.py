from app.risk.datasets.bankruptcy_dataset import (
    BankruptcyDataset,
)

from app.risk.preprocessing.bankruptcy_preprocessor import (
    BankruptcyPreprocessor,
)

from app.risk.models.bankruptcy_model import (
    BankruptcyModel,
)

from app.risk.pipeline.bankruptcy_pipeline import (
    BankruptcyPipeline,
)

from app.risk.explainability.bankruptcy_shap import (
    BankruptcySHAP,
)

from app.risk.dashboard.bankruptcy_dashboard import (
    BankruptcyDashboard,
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

model.fit(

    processed["X_train"],

    processed["y_train"],

)

##############################################################

sample = data["X"].iloc[[0]]

##############################################################

prediction = BankruptcyPipeline.predict(

    sample

)

##############################################################

explainer = BankruptcySHAP(

    model.model

)

shap_results = explainer.explain(

    sample,

    top_n=5,

)

##############################################################

dashboard = BankruptcyDashboard.company_report(

    prediction,

    shap_results,

)

##############################################################

print()

print("=" * 60)

print("BANKRUPTCY DASHBOARD")

print("=" * 60)

print()

for key, value in dashboard.items():

    print(

        key,

        ":",

        value,

    )