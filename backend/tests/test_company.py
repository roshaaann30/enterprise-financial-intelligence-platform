from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_company():

    response = client.get("/company")

    assert response.status_code == 200