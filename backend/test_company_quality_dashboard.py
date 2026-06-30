import pandas as pd

from app.risk.pipeline.company_quality_pipeline import (
    CompanyQualityPipeline,
)

from app.risk.models.company_quality_model import (
    CompanyQualityModel,
)

from app.risk.explainability.company_quality_shap import (
    CompanyQualitySHAP,
)

from app.risk.dashboard.company_quality_dashboard import (
    CompanyQualityDashboard,
)

###########################################################

prediction = (

    CompanyQualityPipeline.predict(

        financial_health=91,

        bankruptcy_risk=8,

        credit_risk=12,

        investment_score=84,

    )

)

###########################################################

sample = pd.DataFrame(

    {

        "FinancialHealth": [91],

        "BankruptcyRisk": [8],

        "CreditRisk": [12],

        "InvestmentScore": [84],

    }

)

###########################################################

model = CompanyQualityModel.load()

explainer = CompanyQualitySHAP(

    model

)

shap_results = explainer.explain(

    sample,

    top_n=4,

)

###########################################################

dashboard = (

    CompanyQualityDashboard.company_report(

        prediction,

        shap_results,

    )

)

###########################################################

print()

print("=" * 60)

print("COMPANY QUALITY DASHBOARD")

print("=" * 60)

print()

for key, value in dashboard.items():

    print(

        key,

        ":",

        value,

    )