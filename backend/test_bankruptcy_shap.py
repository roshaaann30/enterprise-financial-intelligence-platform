from app.risk.datasets.bankruptcy_dataset import (
    BankruptcyDataset,
)

from app.risk.preprocessing.bankruptcy_preprocessor import (
    BankruptcyPreprocessor,
)

from app.risk.models.bankruptcy_model import (
    BankruptcyModel,
)

from app.risk.explainability.bankruptcy_shap import (
    BankruptcySHAP,
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

explainer = BankruptcySHAP(

    model.model

)

##############################################################

results = explainer.explain(

    sample,

    top_n=10,

)

##############################################################

print()

print("=" * 60)

print("TOP SHAP FEATURES")

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