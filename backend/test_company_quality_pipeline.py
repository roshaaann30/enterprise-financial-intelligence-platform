from app.risk.pipeline.company_quality_pipeline import (
    CompanyQualityPipeline,
)

###########################################################

result = CompanyQualityPipeline.predict(

    financial_health=91,

    bankruptcy_risk=8,

    credit_risk=12,

    investment_score=84,

)

###########################################################

print()

print("=" * 60)

print("COMPANY QUALITY PIPELINE")

print("=" * 60)

print()

for key, value in result.items():

    print(

        key,

        ":",

        value,

    )