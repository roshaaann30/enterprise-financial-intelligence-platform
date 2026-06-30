from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_scenario():

    response = client.post(
        "/scenario",
        json={
            "revenue_change": -10,
            "interest_change": 2,
            "inflation_change": 3,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert "risk_score" in data

    assert "confidence" in data