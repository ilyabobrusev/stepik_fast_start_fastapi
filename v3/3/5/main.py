from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/")
def root(response: Response):
    response.headers["Secret-Code"] = "123459"
    response.headers["Secret-Word"] = "Word"
    return {"message": "Hello from my api"}
