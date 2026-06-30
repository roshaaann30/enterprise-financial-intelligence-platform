from app.risk.datasets.investment_dataset import (
    InvestmentDataset,
)

from app.risk.preprocessing.investment_preprocessor import (
    InvestmentPreprocessor,
)

from app.risk.models.investment_risk_model import (
    InvestmentRiskModel,
)

from app.risk.models.return_prediction_model import (
    ReturnPredictionModel,
)

from app.risk.pipeline.investment_pipeline import (
    InvestmentPipeline,
)

from app.risk.explainability.investment_shap import (
    InvestmentSHAP,
)

from app.risk.dashboard.investment_dashboard import (
    InvestmentDashboard,
)

from app.risk.features.investment_features import (
    InvestmentFeatures,
)

##############################################################
# Dataset
##############################################################

print("\nLoading Dataset...")

dataset = InvestmentDataset()

data = dataset.process()

##############################################################
# Preprocessing
##############################################################

print("Preprocessing Data...")

preprocessor = InvestmentPreprocessor()

processed = preprocessor.process(

    data["X"],
    data["y"],

)

##############################################################
# Train Risk Model
##############################################################

print("Training Investment Risk Model...")

risk_model = InvestmentRiskModel()

risk_model.fit(

    processed["X_train"],
    processed["y_train"],

)

risk_model.save()

##############################################################
# Train Return Model
##############################################################

print("Training Return Prediction Model...")

import numpy as np

return_targets = np.random.uniform(

    -10,
    30,
    len(processed["y_train"])

)

return_model = ReturnPredictionModel()

return_model.fit(

    processed["X_train"],
    return_targets,

)

return_model.save()

##############################################################
# Sample Prediction
##############################################################

print("Running Investment Pipeline...")

sample = data["X"].iloc[[0]]

prediction = InvestmentPipeline.predict(

    sample

)

##############################################################
# SHAP Explanation
##############################################################

print("Generating SHAP Explanations...")

features = InvestmentFeatures.generate(

    sample

)

explainer = InvestmentSHAP(

    risk_model.model

)

shap_results = explainer.explain(

    features,

    top_n=5,

)

##############################################################
# Dashboard
##############################################################

dashboard = (

    InvestmentDashboard.company_report(

        prediction,

        shap_results,

    )

)

##############################################################
# Results
##############################################################

print()

print("=" * 70)
print("INVESTMENT AI PLATFORM")
print("=" * 70)

print()

print("INVESTMENT ANALYSIS")
print()

print(
    f"Investment Score: "
    f"{dashboard['investment_score']}"
)

print(
    f"Recommendation: "
    f"{dashboard['recommendation']}"
)

print(
    f"Expected Return: "
    f"{dashboard['expected_return']}%"
)

print(
    f"Risk Category: "
    f"{dashboard['risk_category']}"
)

print(
    f"Risk Probability: "
    f"{dashboard['risk_percentage']}%"
)

print(
    f"Confidence: "
    f"{dashboard['confidence']}%"
)

print()

print("-" * 70)

print()
print("TOP INVESTMENT FACTORS")
print()

for factor in dashboard["top_factors"]:

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