from fastapi import FastAPI, HTTPException
from typing import Optional
import httpx

app = FastAPI()

# Имитация базы данных
fake_db = {
    1: {"id": 1, "name": "Item 1", "description": "This is item 1"},
    2: {"id": 2, "name": "Item 2", "description": "This is item 2"},
}

# Имитация внешнего API
async def fetch_external_data(item_id: int) -> Optional[dict]:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://external-api.com/items/{item_id}")
        if response.status_code == 200:
            return response.json()
        return None

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    item = fake_db.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.get("/external-items/{item_id}")
async def read_external_item(item_id: int):
    try:
        external_data = await fetch_external_data(item_id)
        if external_data is None:
            raise HTTPException(status_code=404, detail="External item not found")
        return external_data
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"External API request failed: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")