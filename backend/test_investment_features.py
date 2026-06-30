import pandas as pd

from app.risk.features.investment_features import (
    InvestmentFeatures,
)

###########################################################

data = pd.DataFrame(

    {

        "NetIncome": [50000],

        "ShareholderEquity": [250000],

        "TotalAssets": [800000],

        "TotalLiabilities": [300000],

        "CurrentAssets": [150000],

        "CurrentLiabilities": [75000],

        "Inventory": [25000],

        "Revenue": [1200000],

        "PreviousRevenue": [1000000],

        "OperatingIncome": [180000],

        "PreviousNetIncome": [40000],

        "OperatingCashFlow": [140000],

        "EBIT": [200000],

        "InterestExpense": [25000],

    }

)

###########################################################

features = InvestmentFeatures.generate(

    data

)

###########################################################

print()

print("=" * 60)

print("INVESTMENT FEATURES")

print("=" * 60)

print()

print(features)