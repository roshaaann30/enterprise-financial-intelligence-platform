from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_every_endpoint():

    endpoints = [

        "/dashboard",

        "/company",

        "/forecast",

        "/monitoring",

        "/system",

    ]

    for endpoint in endpoints:

        response = client.get(endpoint)

        assert response.status_code == 200