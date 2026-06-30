# backend/app/api/forecast_api.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/forecast")
def get_forecast():

    return {

        "revenue_growth": 12.5,

        "forecast_confidence": 84

    }