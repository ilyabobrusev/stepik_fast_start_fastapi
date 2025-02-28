from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_register_user():
    response = client.post("/register", json={"username": "testuser", "email": "test@example.com"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "username": "testuser", "email": "test@example.com"}

def test_get_user():
    # Сначала регистрируем пользователя
    client.post("/register", json={"username": "testuser", "email": "test@example.com"})
    
    # Теперь получаем пользователя
    response = client.get("/user/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "username": "testuser", "email": "test@example.com"}

def test_get_user_not_found():
    response = client.get("/user/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}

def test_delete_user():
    # Сначала регистрируем пользователя
    client.post("/register", json={"username": "testuser", "email": "test@example.com"})
    
    # Теперь удаляем пользователя
    response = client.delete("/user/1")
    assert response.status_code == 200
    assert response.json() == {"message": "User deleted"}
    
    # Проверяем, что пользователь действительно удален
    response = client.get("/user/1")
    assert response.status_code == 404

def test_delete_user_not_found():
    response = client.delete("/user/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}

# Mock test
from unittest.mock import patch

def test_register_user_with_mock():
    with patch("main.users_db", {}):
        response = client.post("/register", json={"username": "mockuser", "email": "mock@example.com"})
        assert response.status_code == 200
        assert response.json() == {"id": 1, "username": "mockuser", "email": "mock@example.com"}
