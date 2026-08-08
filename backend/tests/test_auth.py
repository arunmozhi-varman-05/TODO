import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_and_login():
    email = "testuser@example.com"
    password = "SecurePassword123!"

    # 1. Register User
    response = client.post(
        "/api/v1/auth/register",
        json={"email": email, "password": password, "full_name": "Test User"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == email
    assert "id" in data

    # 2. Duplicate registration attempt should fail
    response_dup = client.post(
        "/api/v1/auth/register",
        json={"email": email, "password": password}
    )
    assert response_dup.status_code == 400

    # 3. Login with credentials
    login_response = client.post(
        "/api/v1/auth/login",
        data={"username": email, "password": password}
    )
    assert login_response.status_code == 200
    token_data = login_response.json()
    assert "access_token" in token_data
    assert token_data["token_type"] == "bearer"
