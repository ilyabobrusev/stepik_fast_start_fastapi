import pytest
from fastapi.testclient import TestClient
from main import app, Base, get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

TEST_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture
def test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_create_user(test_db):
    response = client.post(
        "/users/",
        json={"username": "testuser", "email": "test@example.com", "full_name": "Test User"},
    )
    assert response.status_code == 200
    assert response.json() == {"username": "testuser", "email": "test@example.com", "full_name": "Test User"}

def test_read_user(test_db):
    client.post(
        "/users/",
        json={"username": "testuser", "email": "test@example.com", "full_name": "Test User"},
    )
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == {"username": "testuser", "email": "test@example.com", "full_name": "Test User"}

def test_update_user(test_db):
    client.post(
        "/users/",
        json={"username": "testuser", "email": "test@example.com", "full_name": "Test User"},
    )
    response = client.put(
        "/users/1",
        json={"email": "updated@example.com", "full_name": "Updated User"},
    )
    assert response.status_code == 200
    assert response.json() == {"username": "testuser", "email": "updated@example.com", "full_name": "Updated User"}

def test_read_nonexistent_user(test_db):
    response = client.get("/users/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}

def test_update_nonexistent_user(test_db):
    response = client.put(
        "/users/999",
        json={"email": "updated@example.com", "full_name": "Updated User"},
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}