from app.risk.scoring.company_quality_score import (
    CompanyQualityScore,
)

###########################################################

result = CompanyQualityScore.calculate(

    financial_health_score=91,

    bankruptcy_risk=8,

    credit_risk=12,

    investment_score=84,

)

###########################################################

print()

print("=" * 60)

print("COMPANY QUALITY SCORE")

print("=" * 60)

print()

for key, value in result.items():

    print(

        key,

        ":",

        value,

    )