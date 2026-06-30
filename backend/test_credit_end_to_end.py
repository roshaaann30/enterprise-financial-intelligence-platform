from app.risk.datasets.credit_dataset import (
    CreditDataset,
)

from app.risk.preprocessing.credit_preprocessor import (
    CreditPreprocessor,
)

from app.risk.models.credit_risk_model import (
    CreditRiskModel,
)

from app.risk.trainers.credit_trainer import (
    CreditTrainer,
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

##############################################################
# Load Dataset
##############################################################

print("\nLoading Credit Dataset...")

dataset = CreditDataset()

data = dataset.process()

##############################################################
# Preprocess
##############################################################

print("Preprocessing Dataset...")

preprocessor = CreditPreprocessor()

processed = preprocessor.process(
    data["X"],
    data["y"],
)

##############################################################
# Train Model
##############################################################

print("Training Credit Risk Model...")

model = CreditRiskModel()

trainer = CreditTrainer(
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
# Sample Prediction
##############################################################

print("Generating Prediction...")

sample = data["X"].iloc[[0]]

prediction = CreditPipeline.predict(
    sample
)

##############################################################
# SHAP Explainability
##############################################################

print("Generating SHAP Explanations...")

explainer = CreditSHAP(
    model.model
)

shap_results = explainer.explain(
    sample,
    top_n=5,
)

##############################################################
# Dashboard
##############################################################

dashboard = CreditDashboard.borrower_report(
    prediction,
    shap_results,
)

##############################################################
# Results
##############################################################

print()

print("=" * 70)
print("CREDIT RISK PREDICTION SYSTEM")
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
print("CREDIT ASSESSMENT")
print()

print(
    f"Credit Score: "
    f"{dashboard['credit_score']}"
)

print(
    f"Risk Category: "
    f"{dashboard['risk_category']}"
)

print(
    f"Default Probability: "
    f"{dashboard['default_percentage']}%"
)

print(
    f"Confidence: "
    f"{dashboard['confidence']}%"
)

print()
print("-" * 70)

print()
print("TOP CREDIT FACTORS")
print()

for factor in dashboard["top_risk_factors"]:

    print(
        f"{factor['feature']} "
        f"=> "
        f"{factor['impact']} "
        f"({factor['direction']})"
    )

print()

print("=" * 70)
print("SYSTEM TEST PASSED")
print("=" * 70)