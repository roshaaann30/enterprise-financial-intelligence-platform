from app.scenario.scenario_engine import (
    ScenarioEngine,
)


class InflationSimulator:

    @staticmethod
    def simulate(

        inflation_increase,

    ):

        revenue = (

            inflation_increase

            * 0.5

        )

        profit = (

            -inflation_increase

            * 1.2

        )

        risk = (

            inflation_increase

            * 0.7

        )

        return (

            ScenarioEngine.build_result(

                "Inflation Shock",

                revenue,

                profit,

                risk,

            )

        )