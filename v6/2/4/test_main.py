from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user_valid():
    response = client.post(
        "/user/",
        json={
            "username": "testuser",
            "age": 25,
            "email": "test@example.com",
            "password": "password123",
            "phone": "1234567890"
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "message": "User created successfully",
        "user": {
            "username": "testuser",
            "age": 25,
            "email": "test@example.com",
            "password": "password123",
            "phone": "1234567890"
        }
    }

def test_create_user_invalid_age():
    response = client.post(
        "/user/",
        json={
            "username": "testuser",
            "age": 17,
            "email": "test@example.com",
            "password": "password123",
            "phone": "1234567890"
        },
    )
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "ensure this value is greater than 18"

def test_create_user_invalid_email():
    response = client.post(
        "/user/",
        json={
            "username": "testuser",
            "age": 25,
            "email": "invalid-email",
            "password": "password123",
            "phone": "1234567890"
        },
    )
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "value is not a valid email address"

def test_create_user_invalid_password_length():
    response = client.post(
        "/user/",
        json={
            "username": "testuser",
            "age": 25,
            "email": "test@example.com",
            "password": "pass",
            "phone": "1234567890"
        },
    )
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "ensure this value has at least 8 characters"
