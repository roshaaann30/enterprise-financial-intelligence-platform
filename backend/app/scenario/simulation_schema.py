from dataclasses import dataclass


@dataclass
class ScenarioResult:

    scenario_name: str

    revenue_impact: float

    profit_impact: float

    risk_score_change: float

    recommendation: str

    simulation_only: bool = True