from unittest.mock import MagicMock

from fastapi.testclient import TestClient

from src.main import app


client = TestClient(app)


def test_health(monkeypatch: MagicMock):
    monkeypatch.setenv("POSTGRES_USER", "test")
    monkeypatch.setenv("POSTGRES_PASSWORD", "test")
    monkeypatch.setenv("POSTGRES_DB", "test")
    monkeypatch.setenv("POSTGRES_HOST", "localhost")

    response = client.get("/v1/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}
