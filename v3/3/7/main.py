from fastapi import FastAPI, Request, HTTPException

app = FastAPI()


@app.get("/headers")
async def get_headers(request: Request):
    user_agent = request.headers.get("user-agent")
    accept_language = request.headers.get("accept-language")

    if user_agent is None or accept_language is None:
        raise HTTPException(status_code=400, detail="Missing required headers")

    response_data = {
        "User-Agent": user_agent,
        "Accept-Language": accept_language
    }

    return response_data
