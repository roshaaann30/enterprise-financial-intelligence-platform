from fastapi import APIRouter

router = APIRouter()


@router.get("/explainability")
def explainability():

    return {

        "prediction": "Buy",

        "confidence": 91,

        "top_features": [

            {
                "feature": "Revenue Growth",
                "importance": 32
            },

            {
                "feature": "Profit Margin",
                "importance": 25
            },

            {
                "feature": "Cash Flow",
                "importance": 18
            },

            {
                "feature": "Debt Ratio",
                "importance": 15
            },

            {
                "feature": "Market Volatility",
                "importance": 10
            }

        ],

        "models": [

            {
                "name": "Random Forest",
                "score": 91
            },

            {
                "name": "XGBoost",
                "score": 94
            },

            {
                "name": "Linear Regression",
                "score": 82
            }

        ]

    }