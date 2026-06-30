from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_dashboard():

    response = client.get("/dashboard")

    assert response.status_code == 200

    data = response.json()

    assert "risk_score" in data

    assert "forecast_score" in data