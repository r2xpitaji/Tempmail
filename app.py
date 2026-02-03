from fastapi import FastAPI, Query
import random
import string
import httpx

app = FastAPI()

@app.get("/")
def home():
    return {"status": "working", "message": "TempMail API Live"}

@app.get("/create")
def create_email():
    domain = "1secmail.com"
    login = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
    email = f"{login}@{domain}"
    return {"email": email, "login": login, "domain": domain}

@app.get("/inbox")
async def get_inbox(login: str = Query(...), domain: str = Query(...)):
    url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}"
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        return r.json()

@app.get("/message")
async def read_message(login: str = Query(...), domain: str = Query(...), id: int = Query(...)):
    url = f"https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={id}"
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        return r.json()