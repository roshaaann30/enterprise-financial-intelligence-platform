from fastapi import APIRouter

router = APIRouter()


@router.post("/scenario")
def scenario(data: dict):

    revenue_change = float(
        data.get("revenue_change", 0)
    )

    interest_change = float(
        data.get("interest_change", 0)
    )

    inflation_change = float(
        data.get("inflation_change", 0)
    )

    risk_score = (
        35
        + abs(revenue_change)
        + interest_change * 2
        + inflation_change
    )

    return {

        "forecast_impact":
            revenue_change * 1.2,

        "risk_score":
            round(risk_score, 2),

        "confidence":
            87,

        "assessment":
            "Moderately Negative"

    }