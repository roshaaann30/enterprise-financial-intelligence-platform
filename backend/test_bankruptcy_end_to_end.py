from app.risk.datasets.bankruptcy_dataset import (
    BankruptcyDataset,
)

from app.risk.preprocessing.bankruptcy_preprocessor import (
    BankruptcyPreprocessor,
)

from app.risk.models.bankruptcy_model import (
    BankruptcyModel,
)

from app.risk.trainers.bankruptcy_trainer import (
    BankruptcyTrainer,
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
# Load Dataset
##############################################################

print("\nLoading Dataset...")

dataset = BankruptcyDataset()

data = dataset.process()

##############################################################
# Preprocess
##############################################################

print("Preprocessing Dataset...")

preprocessor = BankruptcyPreprocessor()

processed = preprocessor.process(

    data["X"],

    data["y"],

)

##############################################################
# Train Model
##############################################################

print("Training Model...")

model = BankruptcyModel()

trainer = BankruptcyTrainer(

    model

)

trainer.train(

    processed["X_train"],

    processed["y_train"],

)

##############################################################
# Evaluate
##############################################################

print("Evaluating Model...")

evaluation = trainer.evaluate(

    processed["X_test"],

    processed["y_test"],

)

##############################################################
# Save Model
##############################################################

model.save()

##############################################################
# Prediction
##############################################################

print("Generating Prediction...")

sample = data["X"].iloc[[0]]

prediction = BankruptcyPipeline.predict(

    sample

)

##############################################################
# SHAP
##############################################################

print("Generating SHAP Explanations...")

explainer = BankruptcySHAP(

    model.model

)

shap_results = explainer.explain(

    sample,

    top_n=5,

)

##############################################################
# Dashboard
##############################################################

dashboard = BankruptcyDashboard.company_report(

    prediction,

    shap_results,

)

##############################################################
# Output
##############################################################

print()

print("=" * 70)

print("BANKRUPTCY RISK PREDICTION SYSTEM")

print("=" * 70)

print()

print("MODEL METRICS")

print()

for metric, value in evaluation["metrics"].items():

    print(

        f"{metric}: {value:.4f}"

    )

print()

print("-" * 70)

print()

print("PREDICTION")

print()

print(

    f"Probability: "

    f"{dashboard['bankruptcy_percentage']}%"

)

print(

    f"Risk Level: "

    f"{dashboard['risk_level']}"

)

print(

    f"Confidence: "

    f"{dashboard['confidence']}%"

)

print()

print("-" * 70)

print()

print("TOP RISK FACTORS")

print()

for factor in dashboard["top_risk_factors"]:

    print(

        f"{factor['feature']} "

        f"=> "

        f"{factor['impact']}"

    )

print()

print("=" * 70)

print("SYSTEM TEST PASSED")

print("=" * 70)