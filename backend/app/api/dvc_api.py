from fastapi import APIRouter

router = APIRouter()

@router.get("/dvc-status")
def dvc_status():
    return {
        "dvc_enabled": True,
        "datasets": 1,
        "tracked_file": "sample_financials.csv",
        "status": "Version Controlled"
    }