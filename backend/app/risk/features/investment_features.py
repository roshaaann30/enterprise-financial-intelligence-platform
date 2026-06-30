import pandas as pd


class InvestmentFeatures:

    """
    Enterprise Investment Feature Engineering
    """

    ###########################################################
    # Return on Equity
    ###########################################################

    @staticmethod
    def roe(

        net_income,

        shareholder_equity,

    ):

        return net_income / shareholder_equity

    ###########################################################
    # Return on Assets
    ###########################################################

    @staticmethod
    def roa(

        net_income,

        total_assets,

    ):

        return net_income / total_assets

    ###########################################################
    # Debt Ratio
    ###########################################################

    @staticmethod
    def debt_ratio(

        total_liabilities,

        total_assets,

    ):

        return total_liabilities / total_assets

    ###########################################################
    # Current Ratio
    ###########################################################

    @staticmethod
    def current_ratio(

        current_assets,

        current_liabilities,

    ):

        return current_assets / current_liabilities

    ###########################################################
    # Quick Ratio
    ###########################################################

    @staticmethod
    def quick_ratio(

        current_assets,

        inventory,

        current_liabilities,

    ):

        return (

            current_assets - inventory

        ) / current_liabilities

    ###########################################################
    # Profit Margin
    ###########################################################

    @staticmethod
    def profit_margin(

        net_income,

        revenue,

    ):

        return net_income / revenue

    ###########################################################
    # Operating Margin
    ###########################################################

    @staticmethod
    def operating_margin(

        operating_income,

        revenue,

    ):

        return operating_income / revenue

    ###########################################################
    # Asset Turnover
    ###########################################################

    @staticmethod
    def asset_turnover(

        revenue,

        total_assets,

    ):

        return revenue / total_assets

    ###########################################################
    # Revenue Growth
    ###########################################################

    @staticmethod
    def revenue_growth(

        current_revenue,

        previous_revenue,

    ):

        return (

            current_revenue

            - previous_revenue

        ) / previous_revenue

    ###########################################################
    # Earnings Growth
    ###########################################################

    @staticmethod
    def earnings_growth(

        current_income,

        previous_income,

    ):

        return (

            current_income

            - previous_income

        ) / previous_income

    ###########################################################
    # Cash Flow Ratio
    ###########################################################

    @staticmethod
    def cash_flow_ratio(

        operating_cash_flow,

        current_liabilities,

    ):

        return (

            operating_cash_flow

            / current_liabilities

        )

    ###########################################################
    # Interest Coverage
    ###########################################################

    @staticmethod
    def interest_coverage(

        ebit,

        interest_expense,

    ):

        return ebit / interest_expense

    ###########################################################
    # Generate Features
    ###########################################################

    @staticmethod
    def generate(

        df,

    ):

        features = pd.DataFrame()

        features["ROE"] = (
            df["NetIncome"]
            /
            df["ShareholderEquity"]
        )

        features["ROA"] = (
            df["NetIncome"]
            /
            df["TotalAssets"]
        )

        features["DebtRatio"] = (
            df["TotalLiabilities"]
            /
            df["TotalAssets"]
        )

        features["CurrentRatio"] = (
            df["CurrentAssets"]
            /
            df["CurrentLiabilities"]
        )

        features["QuickRatio"] = (
            (
                df["CurrentAssets"]
                -
                df["Inventory"]
            )
            /
            df["CurrentLiabilities"]
        )

        features["ProfitMargin"] = (
            df["NetIncome"]
            /
            df["Revenue"]
        )

        features["OperatingMargin"] = (
            df["OperatingIncome"]
            /
            df["Revenue"]
        )

        features["AssetTurnover"] = (
            df["Revenue"]
            /
            df["TotalAssets"]
        )

        features["RevenueGrowth"] = (
            (
                df["Revenue"]
                -
                df["PreviousRevenue"]
            )
            /
            df["PreviousRevenue"]
        )

        features["EarningsGrowth"] = (
            (
                df["NetIncome"]
                -
                df["PreviousNetIncome"]
            )
            /
            df["PreviousNetIncome"]
        )

        features["CashFlowRatio"] = (
            df["OperatingCashFlow"]
            /
            df["CurrentLiabilities"]
        )

        features["InterestCoverage"] = (
            df["EBIT"]
            /
            df["InterestExpense"]
        )

        return features.fillna(0)