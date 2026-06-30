from app.scenario.scenario_engine import (
    ScenarioEngine,
)


class RevenueShockSimulator:

    @staticmethod
    def simulate(

        revenue_decline_pct,

    ):

        revenue_impact = (

            -revenue_decline_pct

        )

        profit_impact = (

            -revenue_decline_pct

            * 1.4

        )

        risk_change = (

            revenue_decline_pct

            * 0.8

        )

        return (

            ScenarioEngine.build_result(

                "Revenue Decline",

                revenue_impact,

                profit_impact,

                risk_change,

            )

        )