from app.scenario.scenario_engine import (
    ScenarioEngine,
)


class SupplyChainSimulator:

    @staticmethod
    def simulate(

        disruption_pct,

    ):

        revenue = (

            -disruption_pct

            * 0.8

        )

        profit = (

            -disruption_pct

            * 1.5

        )

        risk = (

            disruption_pct

            * 1.2

        )

        return (

            ScenarioEngine.build_result(

                "Supply Chain Disruption",

                revenue,

                profit,

                risk,

            )

        )