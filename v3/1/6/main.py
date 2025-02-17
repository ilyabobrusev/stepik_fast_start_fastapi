from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

# Пример данных о продуктах
sample_products = [
    {
        "product_id": 123,
        "name": "Smartphone",
        "category": "Electronics",
        "price": 599.99
    },
    {
        "product_id": 456,
        "name": "Phone Case",
        "category": "Accessories",
        "price": 19.99
    },
    {
        "product_id": 789,
        "name": "Iphone",
        "category": "Electronics",
        "price": 1299.99
    },
    {
        "product_id": 101,
        "name": "Headphones",
        "category": "Accessories",
        "price": 99.99
    },
    {
        "product_id": 202,
        "name": "Smartwatch",
        "category": "Electronics",
        "price": 299.99
    }
]

# Конечная точка для получения информации о продукте
@app.get("/product/{product_id}")
async def get_product(product_id: int):
    for product in sample_products:
        if product["product_id"] == product_id:
            return product
    return {"error": "Product not found"}

# Конечная точка для поиска товаров
@app.get("/products/search")
async def search_products(
    keyword: str,
    category: Optional[str] = None,
    limit: int = Query(10, gt=0)
):
    results = []
    for product in sample_products:
        if keyword.lower() in product["name"].lower():
            if category is None or product["category"].lower() == category.lower():
                results.append(product)
                if len(results) >= limit:
                    break
    return results