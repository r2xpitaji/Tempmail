from fastapi import FastAPI, Query
import httpx

app = FastAPI()

@app.get("/")
async def get_inbox(login: str = Query(...), domain: str = Query(...)):
    url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}"

    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        return r.json()