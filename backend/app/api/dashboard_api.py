from fastapi import APIRouter

router = APIRouter()

@router.get("/dashboard")
def get_dashboard():

    return {
        "risk_score": 42,
        "forecast_score": 81,
        "portfolio_score": 76,
        "model_health": 91
    }