import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, AsyncMock
from main import app

client = TestClient(app)

# Тест для конечной точки /items/{item_id}
@pytest.mark.asyncio
async def test_read_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Item 1", "description": "This is item 1"}

    response = client.get("/items/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}

# Тест для конечной точки /external-items/{item_id} (успешный сценарий)
@pytest.mark.asyncio
@patch("main.fetch_external_data", new_callable=AsyncMock)
async def test_read_external_item(mock_fetch_external_data):
    mock_fetch_external_data.return_value = {"id": 1, "name": "External Item 1"}

    response = client.get("/external-items/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "External Item 1"}

    mock_fetch_external_data.return_value = None
    response = client.get("/external-items/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "External item not found"}

# Тест для конечной точки /external-items/{item_id} (ошибка внешнего API)
@pytest.mark.asyncio
@patch("main.fetch_external_data", new_callable=AsyncMock)
async def test_read_external_item_exception(mock_fetch_external_data):
    mock_fetch_external_data.side_effect = Exception("External API error")

    response = client.get("/external-items/1")
    assert response.status_code == 500
    assert response.json() == {"detail": "Internal Server Error: External API error"}