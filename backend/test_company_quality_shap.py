import pandas as pd

from app.risk.models.company_quality_model import (
    CompanyQualityModel,
)

from app.risk.explainability.company_quality_shap import (
    CompanyQualitySHAP,
)

###########################################################

model = CompanyQualityModel.load()

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

explainer = CompanyQualitySHAP(

    model

)

results = explainer.explain(

    sample,

    top_n=4,

)

###########################################################

print()

print("=" * 60)

print("COMPANY QUALITY SHAP")

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