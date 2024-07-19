import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_main():
    response = client.post(
        "/aggregate",
        json={
            "dt_from": "2022-01-01T00:00:00",
            "dt_upto": "2022-12-31T23:59:00",
            "group_type": "month"
        }
    )
    assert response.status_code == 200
    assert "dataset" in response.json()
    assert "labels" in response.json()


def test_invalid_group_type():
    response = client.post(
        "/aggregate",
        json={
            "dt_from": "2022-01-01T00:00:00",
            "dt_upto": "2022-12-31T23:59:00",
            "group_type": "invalid"
        }
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid group_type. Choose from 'hour', 'day', or 'month'"}
