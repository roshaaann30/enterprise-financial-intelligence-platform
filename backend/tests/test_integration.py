from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_dashboard_integration():

    response = client.get("/dashboard")

    assert response.status_code == 200

    data = response.json()

    assert data["risk_score"] > 0

    assert data["forecast_score"] > 0


def test_system_integration():

    response = client.get("/system")

    assert response.status_code == 200

    data = response.json()

    assert data["api_health"] == "Healthy"


def test_scenario_integration():

    response = client.post(
        "/scenario",
        json={
            "revenue_change": -10,
            "interest_change": 2,
            "inflation_change": 3,
        },
    )

    assert response.status_code == 200

    result = response.json()

    assert "risk_score" in result

    assert "confidence" in result