```text
В FastAPI можно использовать операции:

    @app.get()
    @app.post()
    @app.put()
    @app.delete()

И более экзотические:

    @app.options()
    @app.head()
    @app.patch()
    @app.trace()
```
```text
Давайте закрепим разницу в способах определения Path, Query и Body параметров запроса:

1) Path-параметры указывается в маршруте в фигурных скобках {}, а потом в обработчике маршрута:

@app.get("/{some_param}")

async def func_with_path_param(some_param: <type>):

или прописываем явно:

@app.get("/{some_param}")

async def func_with_path_param(some_param: Annotated[<type>, Path()]):

2) Body-параметры представлены в виде Pydantic-моделей и указываются в виде параметра обработчика маршрута с типом соответствующего класса модели (о чем рассказывалось ранее):

@app.post("/")

async def func_with_body_param(user: User):

или прописываем явно:

@app.post("/")

async def func_with_body_param(user: Annotated[User, Body()]):

3) Query-параметры представлены просто в виде параметров обработчика маршрута (объявлены не двумя предыдущими способами):

@app.get("/")

async def func_with_body_param(query_param: <type>):

или указываем явно:

@app.get("/")

async def func_with_body_param(query_param: Annotated[<type>, Query()]):
```