from unittest.mock import patch
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

@patch("app.external_module.requests.get")
def test_get_zones():
    response = client.get("/zones")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data,dict)