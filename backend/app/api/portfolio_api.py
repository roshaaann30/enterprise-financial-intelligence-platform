from fastapi import APIRouter

router = APIRouter()

@router.get("/portfolio")
def get_portfolio():

    return {

        "risk_score": 40,

        "diversification_score": 80,

        "recommendation":
            "Portfolio appears balanced"

    }