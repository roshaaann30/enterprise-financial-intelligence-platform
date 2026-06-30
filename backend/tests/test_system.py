from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_system():

    response = client.get("/system")

    assert response.status_code == 200

    data = response.json()

    assert "api_health" in data