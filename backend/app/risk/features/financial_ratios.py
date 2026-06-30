import numpy as np


class FinancialRatios:

    """
    Enterprise Financial Ratio Engine

    Contains reusable financial ratio calculations used
    throughout the Risk Intelligence Platform.
    """

    ############################################################
    # Safe Division
    ############################################################

    @staticmethod
    def safe_divide(numerator, denominator):

        if denominator is None:
            return 0.0

        if denominator == 0:
            return 0.0

        if np.isnan(denominator):
            return 0.0

        return float(numerator) / float(denominator)

    ############################################################
    # Liquidity
    ############################################################

    @staticmethod
    def current_ratio(

        current_assets,
        current_liabilities,

    ):

        return FinancialRatios.safe_divide(
            current_assets,
            current_liabilities,
        )

    @staticmethod
    def quick_ratio(

        current_assets,
        inventory,
        current_liabilities,

    ):

        return FinancialRatios.safe_divide(
            current_assets - inventory,
            current_liabilities,
        )

    @staticmethod
    def cash_ratio(

        cash,
        current_liabilities,

    ):

        return FinancialRatios.safe_divide(
            cash,
            current_liabilities,
        )

    @staticmethod
    def working_capital(

        current_assets,
        current_liabilities,

    ):

        return current_assets - current_liabilities

    ############################################################
    # Profitability
    ############################################################

    @staticmethod
    def gross_margin(

        revenue,
        cost_of_revenue,

    ):

        gross_profit = revenue - cost_of_revenue

        return FinancialRatios.safe_divide(
            gross_profit,
            revenue,
        )

    @staticmethod
    def operating_margin(

        operating_income,
        revenue,

    ):

        return FinancialRatios.safe_divide(
            operating_income,
            revenue,
        )

    @staticmethod
    def net_margin(

        net_income,
        revenue,

    ):

        return FinancialRatios.safe_divide(
            net_income,
            revenue,
        )

    ############################################################
    # Return Ratios
    ############################################################

    @staticmethod
    def roa(

        net_income,
        total_assets,

    ):

        return FinancialRatios.safe_divide(
            net_income,
            total_assets,
        )

    @staticmethod
    def roe(

        net_income,
        shareholder_equity,

    ):

        return FinancialRatios.safe_divide(
            net_income,
            shareholder_equity,
        )

    @staticmethod
    def roic(

        operating_income,
        invested_capital,

    ):

        return FinancialRatios.safe_divide(
            operating_income,
            invested_capital,
        )

    ############################################################
    # Leverage
    ############################################################

    @staticmethod
    def debt_ratio(

        total_debt,
        total_assets,

    ):

        return FinancialRatios.safe_divide(
            total_debt,
            total_assets,
        )

    @staticmethod
    def debt_to_equity(

        total_debt,
        shareholder_equity,

    ):

        return FinancialRatios.safe_divide(
            total_debt,
            shareholder_equity,
        )

    @staticmethod
    def equity_ratio(

        shareholder_equity,
        total_assets,

    ):

        return FinancialRatios.safe_divide(
            shareholder_equity,
            total_assets,
        )

    ############################################################
    # Coverage
    ############################################################

    @staticmethod
    def interest_coverage(

        ebit,
        interest_expense,

    ):

        return FinancialRatios.safe_divide(
            ebit,
            interest_expense,
        )

    ############################################################
    # Efficiency
    ############################################################

    @staticmethod
    def asset_turnover(

        revenue,
        total_assets,

    ):

        return FinancialRatios.safe_divide(
            revenue,
            total_assets,
        )

    @staticmethod
    def inventory_turnover(

        cost_of_revenue,
        inventory,

    ):

        return FinancialRatios.safe_divide(
            cost_of_revenue,
            inventory,
        )

    @staticmethod
    def receivable_turnover(

        revenue,
        accounts_receivable,

    ):

        return FinancialRatios.safe_divide(
            revenue,
            accounts_receivable,
        )

    ############################################################
    # Cash Flow
    ############################################################

    @staticmethod
    def operating_cashflow_ratio(

        operating_cash_flow,
        current_liabilities,

    ):

        return FinancialRatios.safe_divide(
            operating_cash_flow,
            current_liabilities,
        )

    @staticmethod
    def free_cash_flow(

        operating_cash_flow,
        capital_expenditure,

    ):

        return operating_cash_flow - capital_expenditure

    ############################################################
    # Growth
    ############################################################

    @staticmethod
    def growth_rate(

        current_value,
        previous_value,

    ):

        return FinancialRatios.safe_divide(
            current_value - previous_value,
            previous_value,
        )

    ############################################################
    # Enterprise Value
    ############################################################

    @staticmethod
    def enterprise_value(

        market_cap,
        total_debt,
        cash,

    ):

        return (

            market_cap

            + total_debt

            - cash

        )

    ############################################################
    # EBITDA Multiple
    ############################################################

    @staticmethod
    def ev_to_ebitda(

        enterprise_value,
        ebitda,

    ):

        return FinancialRatios.safe_divide(
            enterprise_value,
            ebitda,
        )