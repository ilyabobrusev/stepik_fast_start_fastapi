```python
# main.py
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# Start app
uvicorn main:app --reload
```

```bash
python3 "/home/q/git/github.com/ilyabobrusev/stepik_fast_start_fastapi/v2/1/main.py"

# or

uvicorn main:app --reload
```