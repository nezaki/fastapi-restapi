from uuid import UUID

from fastapi.testclient import TestClient


class TestCreateUser:
    def test_returns_201_with_user_data(self, client: TestClient):
        response = client.post(
            "/api/v1/users/",
            json={"name": "Alice", "email": "alice@example.com"},
        )

        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "Alice"
        assert data["email"] == "alice@example.com"
        assert UUID(data["id"])  # valid UUID

    def test_response_contains_only_expected_fields(self, client: TestClient):
        response = client.post(
            "/api/v1/users/",
            json={"name": "Bob", "email": "bob@example.com"},
        )

        data = response.json()
        assert set(data.keys()) == {"id", "name", "email"}

    def test_duplicate_email_returns_409(self, client: TestClient):
        payload = {"name": "Charlie", "email": "charlie@example.com"}
        client.post("/api/v1/users/", json=payload)

        response = client.post("/api/v1/users/", json=payload)

        assert response.status_code == 409

    def test_missing_name_returns_422(self, client: TestClient):
        response = client.post(
            "/api/v1/users/",
            json={"email": "noname@example.com"},
        )

        assert response.status_code == 422

    def test_missing_email_returns_422(self, client: TestClient):
        response = client.post(
            "/api/v1/users/",
            json={"name": "NoEmail"},
        )

        assert response.status_code == 422
