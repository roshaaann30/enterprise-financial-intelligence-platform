import pandas as pd

from app.portfolio.portfolio_advisor import (
    EnterprisePortfolioAdvisor,
)

portfolio = pd.DataFrame(

    {

        "symbol": [

            "AAPL",

            "MSFT",

            "GOOG",

            "TSLA",

        ],

        "sector": [

            "Technology",

            "Technology",

            "Technology",

            "Automotive",

        ],

        "weight": [

            30,

            25,

            20,

            25,

        ],

    }

)

result = (

    EnterprisePortfolioAdvisor.analyze(

        portfolio

    )

)

print(result)