#Пример валидации Query-параметров:

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(q: str | None = None): # валидируем тут и задаём значение по-умолчанию
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#Пример валидации Path-параметров:

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int): # задаём тип тут
    return {"item_id": item_id}

#Пример валидации Header-параметров:

from typing import Annotated

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(user_agent: Annotated[str | None, Header()] = None): # задаём тип тут
    return {"User-Agent": user_agent}
