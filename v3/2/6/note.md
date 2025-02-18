```text
Также у класса Response есть метод delete_cookie, который принимает в качестве аргумента строку (наименование куки) и удаляет ее на стороне клиента.

Под капотом, этот метод вызывает метод set_cookie и устанавливает атрибутам max_age и expires значение 0.
```

### Для примера:
```python
@router.post("/logout", status_code=204)
async def logout_user(response: Response):
    response.delete_cookie("example_access_token")
```
