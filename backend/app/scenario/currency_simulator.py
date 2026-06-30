from app.scenario.scenario_engine import (
    ScenarioEngine,
)


class CurrencySimulator:

    @staticmethod
    def simulate(

        fx_change_pct,

    ):

        revenue = (

            fx_change_pct

            * 0.3

        )

        profit = (

            fx_change_pct

            * 0.2

        )

        risk = (

            abs(

                fx_change_pct

            )

            * 0.4

        )

        return (

            ScenarioEngine.build_result(

                "Currency Fluctuation",

                revenue,

                profit,

                risk,

            )

        )