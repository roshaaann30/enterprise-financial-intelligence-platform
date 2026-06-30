from app.scenario.simulation_schema import (
    ScenarioResult,
)


class ScenarioEngine:

    @staticmethod
    def build_result(

        scenario_name,

        revenue_impact,

        profit_impact,

        risk_score_change,

    ):

        return ScenarioResult(

            scenario_name=scenario_name,

            revenue_impact=round(

                revenue_impact,

                2,

            ),

            profit_impact=round(

                profit_impact,

                2,

            ),

            risk_score_change=round(

                risk_score_change,

                2,

            ),

            recommendation=(

                "Simulation Output Only"

            ),

        )