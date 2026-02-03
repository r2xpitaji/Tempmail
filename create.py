from fastapi import FastAPI
import random
import string

app = FastAPI()

@app.get("/")
def create_email():
    domain = "1secmail.com"
    login = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
    email = f"{login}@{domain}"

    return {
        "email": email,
        "login": login,
        "domain": domain
    }