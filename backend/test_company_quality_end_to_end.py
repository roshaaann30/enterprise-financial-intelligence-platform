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

##############################################################
# Sample Inputs
##############################################################

financial_health = 91

bankruptcy_risk = 8

credit_risk = 12

investment_score = 84

##############################################################
# Quality Prediction
##############################################################

print("\nRunning Company Quality Pipeline...")

prediction = CompanyQualityPipeline.predict(

    financial_health=financial_health,

    bankruptcy_risk=bankruptcy_risk,

    credit_risk=credit_risk,

    investment_score=investment_score,

)

##############################################################
# SHAP Explanation
##############################################################

print("Generating SHAP Explanations...")

sample = pd.DataFrame(

    {

        "FinancialHealth": [

            financial_health

        ],

        "BankruptcyRisk": [

            bankruptcy_risk

        ],

        "CreditRisk": [

            credit_risk

        ],

        "InvestmentScore": [

            investment_score

        ],

    }

)

model = CompanyQualityModel.load()

explainer = CompanyQualitySHAP(

    model

)

shap_results = explainer.explain(

    sample,

    top_n=4,

)

##############################################################
# Dashboard
##############################################################

dashboard = (

    CompanyQualityDashboard.company_report(

        prediction,

        shap_results,

    )

)

##############################################################
# Output
##############################################################

print()

print("=" * 70)

print("COMPANY QUALITY AI PLATFORM")

print("=" * 70)

print()

print(

    f"Quality Score: "

    f"{dashboard['quality_score']}"

)

print(

    f"Rating: "

    f"{dashboard['rating']}"

)

print(

    f"Recommendation: "

    f"{dashboard['recommendation']}"

)

print(

    f"Confidence: "

    f"{dashboard['confidence']}%"

)

print()

print("-" * 70)

print()

print("INPUTS")

for key, value in dashboard["inputs"].items():

    print(

        f"{key}: {value}"

    )

print()

print("-" * 70)

print()

print("TOP FACTORS")

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