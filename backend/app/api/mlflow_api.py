from fastapi import APIRouter

router = APIRouter()

@router.get("/mlflow-status")
def mlflow_status():

    return {

        "tracking": "Enabled",

        "experiments": 1,

        "latest_model": "Revenue Forecast",

        "status": "Active"

    }