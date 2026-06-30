from fastapi import APIRouter

router = APIRouter()


@router.get("/monitoring")
def monitoring():

    return {

        "model_accuracy": 94,

        "prediction_confidence": 91,

        "drift_score": 2,

        "data_quality": 98,

        "api_health": "Healthy",

        "system_status": "Online",

    }