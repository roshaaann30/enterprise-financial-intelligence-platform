from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_complete_pipeline():

    dashboard = client.get("/dashboard")
    assert dashboard.status_code == 200

    company = client.get("/company")
    assert company.status_code == 200

    forecast = client.get("/forecast")
    assert forecast.status_code == 200

    monitoring = client.get("/monitoring")
    assert monitoring.status_code == 200

    scenario = client.post(
    "/scenario",
    json={
        "revenue_change": 10,
        "cost_change": 5
    }
    )
    assert scenario.status_code == 200

    mlflow = client.get("/mlflow-status")
    assert mlflow.status_code == 200

    dvc = client.get("/dvc-status")
    assert dvc.status_code == 200