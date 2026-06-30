from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_monitoring():

    response = client.get("/monitoring")

    assert response.status_code == 200

    data = response.json()

    assert "model_accuracy" in data