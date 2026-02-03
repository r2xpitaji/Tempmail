from fastapi import FastAPI, Query
import httpx

app = FastAPI()

@app.get("/")
async def read_message(login: str = Query(...), domain: str = Query(...), id: int = Query(...)):
    url = f"https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={id}"

    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        return r.json()