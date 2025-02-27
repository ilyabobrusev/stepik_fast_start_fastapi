from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

# кастомный обработчик исключения для всех HTTPException
async def custom_http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": str(exc)},
    )

# кастомный обработчик исключения для RequestValidationError (Pydantic validation errors - 422 Unprocessable Entity)
async def custom_request_validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content={"message": "Custom Request Validation Error", "errors": exc.errors()},
    )

# тут показываем альтернативный декораторам способ регистрации хэндлеров
app.add_exception_handler(HTTPException, custom_http_exception_handler)
app.add_exception_handler(RequestValidationError, custom_request_validation_exception_handler)

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
async def create_item(item: Item):
    if item.price < 0:
        raise HTTPException(status_code=400, detail="Price must be non-negative")
    return {"message": "Item created successfully", "item": item}
