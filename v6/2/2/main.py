from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

    @validator("price")
    @classmethod
    def validate_price(cls, value):
        if value < 0:
            raise ValueError("Price must be non-negative")
        return value

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    return {"message": "Item created successfully", "item": item}
