from fastapi import FastAPI, Request, HTTPException
import re

app = FastAPI()

# Регулярное выражение для проверки формата Accept-Language
ACCEPT_LANGUAGE_PATTERN = re.compile(r'^[a-zA-Z-]+(,\s*[a-zA-Z-]+(;\s*q=[0-9.]+)?)*$')

@app.get("/headers")
async def get_headers(request: Request):
    # Извлекаем заголовки
    user_agent = request.headers.get("User-Agent")
    accept_language = request.headers.get("Accept-Language")

    # Проверяем наличие заголовков
    if not user_agent or not accept_language:
        raise HTTPException(status_code=400, detail="Missing required headers")

    # Проверяем формат заголовка Accept-Language
    if not ACCEPT_LANGUAGE_PATTERN.match(accept_language):
        raise HTTPException(status_code=400, detail="Invalid Accept-Language header format")

    # Возвращаем JSON-ответ
    return {
        "User-Agent": user_agent,
        "Accept-Language": accept_language
    }
