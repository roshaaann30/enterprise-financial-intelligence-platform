from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_forecast():

    response = client.get("/forecast")

    assert response.status_code == 200