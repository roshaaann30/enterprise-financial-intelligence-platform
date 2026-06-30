from app.scenario.scenario_manager import (
    EnterpriseScenarioManager,
)

baseline = {

    "revenue_growth": 18,

    "risk_score": 42,

    "investment_score": 78,

}

result = (

    EnterpriseScenarioManager.simulate(

        scenario_type="interest_rate",

        value=3,

        baseline=baseline,

    )

)

print(result)