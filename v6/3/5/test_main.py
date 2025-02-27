from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_register_user_valid():
    response = client.post(
        "/register/",
        json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "password123"
        },
    )
    assert response.status_code == 200
    assert response.json()["message"] == "User registered successfully"

def test_register_user_invalid_data():
    response = client.post(
        "/register/",
        json={
            "username": "testuser",
            "email": "invalid-email",
            "password": "pass"
        },
    )
    assert response.status_code == 422
    assert response.json()["error_code"] == "VALIDATION_ERROR"

def test_get_user_not_found():
    response = client.get("/user/nonexistentuser")
    assert response.status_code == 404
    assert response.json()["error_code"] == "USER_NOT_FOUND"

def test_get_user_valid():
    client.post(
        "/register/",
        json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "password123"
        },
    )
    response = client.get("/user/testuser")
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"