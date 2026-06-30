from app.scenario.revenue_shock import (
    RevenueShockSimulator,
)

from app.scenario.inflation_simulator import (
    InflationSimulator,
)

from app.scenario.interest_rate_simulator import (
    InterestRateSimulator,
)

from app.scenario.currency_simulator import (
    CurrencySimulator,
)

from app.scenario.supply_chain_simulator import (
    SupplyChainSimulator,
)


class EnterpriseScenarioManager:

    """
    Enterprise Scenario Simulation Engine

    IMPORTANT:
    Outputs are simulations only and
    should not be interpreted as
    actual forecasts.
    """

    ###########################################################
    # Apply Scenario To Business Metrics
    ###########################################################

    @staticmethod
    def apply_to_company(

        baseline,

        scenario,

    ):

        revenue = baseline.get(

            "revenue_growth",

            10,

        )

        risk_score = baseline.get(

            "risk_score",

            50,

        )

        investment_score = baseline.get(

            "investment_score",

            50,

        )

        #######################################################
        # Adjust Metrics
        #######################################################

        simulated_revenue = (

            revenue

            +

            scenario.revenue_impact

        )

        simulated_risk = (

            risk_score

            +

            scenario.risk_score_change

        )

        simulated_investment = (

            investment_score

            -

            scenario.risk_score_change

            * 0.5

        )

        #######################################################
        # Rating
        #######################################################

        if simulated_investment >= 80:

            rating = "Strong Buy"

        elif simulated_investment >= 65:

            rating = "Buy"

        elif simulated_investment >= 50:

            rating = "Hold"

        elif simulated_investment >= 35:

            rating = "Reduce"

        else:

            rating = "Sell"

        #######################################################
        # Output
        #######################################################

        return {

            "SIMULATION_ONLY": True,

            "scenario":

                scenario.scenario_name,

            "revenue_growth_before":

                revenue,

            "revenue_growth_after":

                round(

                    simulated_revenue,

                    2,

                ),

            "risk_score_before":

                risk_score,

            "risk_score_after":

                round(

                    simulated_risk,

                    2,

                ),

            "investment_score_before":

                investment_score,

            "investment_score_after":

                round(

                    simulated_investment,

                    2,

                ),

            "investment_rating":

                rating,

            "profit_impact":

                scenario.profit_impact,

        }

    ###########################################################
    # Run Scenario
    ###########################################################

    @staticmethod
    def simulate(

        scenario_type,

        value,

        baseline,

    ):

        if scenario_type == "revenue_decline":

            scenario = (

                RevenueShockSimulator

                .simulate(

                    value

                )

            )

        elif scenario_type == "inflation":

            scenario = (

                InflationSimulator

                .simulate(

                    value

                )

            )

        elif scenario_type == "interest_rate":

            scenario = (

                InterestRateSimulator

                .simulate(

                    value

                )

            )

        elif scenario_type == "currency":

            scenario = (

                CurrencySimulator

                .simulate(

                    value

                )

            )

        elif scenario_type == "supply_chain":

            scenario = (

                SupplyChainSimulator

                .simulate(

                    value

                )

            )

        else:

            raise ValueError(

                f"Unknown scenario: {scenario_type}"

            )

        return (

            EnterpriseScenarioManager

            .apply_to_company(

                baseline,

                scenario,

            )

        )

    ###########################################################
    # Stress Test
    ###########################################################

    @staticmethod
    def stress_test(

        baseline,

    ):

        return {

            "revenue_decline":

                EnterpriseScenarioManager

                .simulate(

                    "revenue_decline",

                    15,

                    baseline,

                ),

            "inflation":

                EnterpriseScenarioManager

                .simulate(

                    "inflation",

                    6,

                    baseline,

                ),

            "interest_rate":

                EnterpriseScenarioManager

                .simulate(

                    "interest_rate",

                    3,

                    baseline,

                ),

            "currency":

                EnterpriseScenarioManager

                .simulate(

                    "currency",

                    10,

                    baseline,

                ),

            "supply_chain":

                EnterpriseScenarioManager

                .simulate(

                    "supply_chain",

                    12,

                    baseline,

                ),

        }