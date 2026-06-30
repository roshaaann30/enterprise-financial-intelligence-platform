from app.risk.datasets.investment_dataset import (
    InvestmentDataset,
)

from app.risk.pipeline.investment_pipeline import (
    InvestmentPipeline,
)

from app.risk.models.investment_risk_model import (
    InvestmentRiskModel,
)

from app.risk.preprocessing.investment_preprocessor import (
    InvestmentPreprocessor,
)

from app.risk.features.investment_features import (
    InvestmentFeatures,
)

from app.risk.explainability.investment_shap import (
    InvestmentSHAP,
)

from app.risk.dashboard.investment_dashboard import (
    InvestmentDashboard,
)

###########################################################

dataset = InvestmentDataset()

data = dataset.process()

###########################################################

sample = data["X"].iloc[[0]]

###########################################################

prediction = InvestmentPipeline.predict(

    sample

)

###########################################################

features = InvestmentFeatures.generate(

    sample

)

###########################################################

model = InvestmentRiskModel.load()

###########################################################

explainer = InvestmentSHAP(

    model

)

###########################################################

shap_results = explainer.explain(

    features,

    top_n=5,

)

###########################################################

dashboard = (

    InvestmentDashboard.company_report(

        prediction,

        shap_results,

    )

)

###########################################################

print()

print("=" * 60)

print("INVESTMENT DASHBOARD")

print("=" * 60)

print()

for key, value in dashboard.items():

    print(

        key,

        ":",

        value,

    )