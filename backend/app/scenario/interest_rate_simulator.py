from app.scenario.scenario_engine import (
    ScenarioEngine,
)


class InterestRateSimulator:

    @staticmethod
    def simulate(

        rate_change,

    ):

        revenue = (

            -rate_change

            * 0.4

        )

        profit = (

            -rate_change

            * 1.1

        )

        risk = (

            rate_change

            * 0.9

        )

        return (

            ScenarioEngine.build_result(

                "Interest Rate Shock",

                revenue,

                profit,

                risk,

            )

        )