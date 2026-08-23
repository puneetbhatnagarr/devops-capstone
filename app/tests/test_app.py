import sys

sys.path.insert(0, "app")

from app import app


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "UP"


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.json["status"] == "running"


def test_students():
    client = app.test_client()

    response = client.get("/students")

    assert response.status_code == 200
    assert len(response.json) == 2
