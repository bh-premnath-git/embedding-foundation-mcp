from fastapi.testclient import TestClient

from python.app.main import app


def test_health_endpoint_handles_small_burst() -> None:
    client = TestClient(app)

    for _ in range(25):
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "ok"
